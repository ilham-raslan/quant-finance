
class OISFuture:
    def __init__(self, maturity, market_price, notional=1.0):
        self.maturity = maturity
        self.market_price = market_price
        self.notional = notional
        self.accrual = 0.25

    def market_rate(self):
        return 1 - self.market_price

    def price(self, ois_curve):
        return self.notional * (1 - ois_curve.df(self.maturity) / ois_curve.df(self.maturity + self.accrual))
