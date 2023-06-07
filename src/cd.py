class CD:
    def __init__(self, stock):
        self.stock = stock

    def purchase(self, quantity, credit_card):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            pass