import unittest
from unittest.mock import Mock

from src.cd import CD

class FakeCreditCard:

    def pay(self):
        return True

class Chart:
    def submit(self,cd):
        pass


class TestPurchaseCD(unittest.TestCase):

    def test_in_stock_payment_accepted(self):
        cd = CD(10)
        credit_card = FakeCreditCard()
        credit_card.pay = lambda: True
        cd.purchase(5, credit_card)
        self.assertEqual(cd.stock, 5)

    def test_not_in_stock(self):
        cd = CD(10)
        credit_card = FakeCreditCard()
        credit_card.pay = lambda: False
        cd.purchase(12, credit_card)
        self.assertEqual(cd.stock, 10)

    def test_payment_rejected(self):
        cd = CD(10)
        credit_card = FakeCreditCard()
        credit_card.pay = lambda: False
        cd.purchase(5, credit_card)
        self.assertEqual(cd.stock, 10)

    def test_notify_chart_when_purchase_with_stock_and_valid_card(self):
        cd = CD(20)
        credit_card = FakeCreditCard()
        credit_card.pay = lambda: True
        chart = Chart()
        chart.submit = Mock(return_value=True)
        cd.purchase(12,credit_card)
        chart.submit.assert_called_with(12)

if __name__ == '__main__':
    unittest.main()
