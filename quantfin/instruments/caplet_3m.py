import math
from scipy.stats import norm

class Caplet3M:
    def __init__(self, expiry, strike, notional=1, market_vol=None):
        self.expiry = expiry
        self.strike = strike
        self.notional = notional
        self.market_vol = market_vol
        self.accrual = 0.25

    def forward_rate(self, ibor_curve):
        return ibor_curve.forward_rate(self.expiry, self.expiry + self.accrual)

    def price(self, ois_curve, ibor_curve, vol_surface):
        notional = self.notional
        expiry = self.expiry
        strike = self.strike
        forward = self.forward_rate(ibor_curve)
        accrual = self.accrual
        df = ois_curve.df(expiry)
        sigma = vol_surface.get_vol(expiry, strike, forward)
        d_1 = (math.log(forward / strike) + (sigma ** 2) * expiry / 2) / (sigma * math.sqrt(expiry))
        d_2 = d_1 - sigma * math.sqrt(expiry)

        price = notional * accrual * df * (forward * norm.cdf(d_1) - strike * norm.cdf(d_2))

        return price
