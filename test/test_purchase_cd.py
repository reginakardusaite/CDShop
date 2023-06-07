import unittest

class CD:
    def __init__(self, stock):
        self.stock = stock

    def purchase(self, quantity, credit_card):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            pass


class FakeCreditCard:

    def pay(self, amount):
        return True


class TestPurchaseCD(unittest.TestCase):
    def test_in_stock_payment_accepted(self):
        cd = CD(10)
        credit_card = FakeCreditCard()
        cd.purchase(5, credit_card)
        self.assertEqual(cd.stock, 5)

    def test_not_in_stock(self):
        cd = CD(10)
        credit_card = FakeCreditCard()
        cd.purchase(12, credit_card)
        self.assertEqual(cd.stock, 10)

if __name__ == '__main__':
    unittest.main()
