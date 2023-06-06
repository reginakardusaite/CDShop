import unittest

class CD:
    def __init__(self, stock):
        self.stock = stock

    def purchase(self, quantity, credit_card):
        pass


class FakeCreditCard:
    def pay(self, amount):
        return True


class TestPurchaseCD(unittest.TestCase):
    def test_in_stock_payment_accepted(self):
        cd = CD(10)
        credit_card = FakeCreditCard()
        cd.purchase(5, credit_card)
        self.assertEqual(cd.stock,5)  # add assertion here


if __name__ == '__main__':
    unittest.main()
