import unittest

from src.cd import CD

class FakeCreditCard:

    def pay(self):
        return True


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

if __name__ == '__main__':
    unittest.main()
