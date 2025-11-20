import numpy as np

class OISSwap:
    def __init__(self, maturity, fixed_rate, notional=1.0):
        self.maturity = maturity
        self.fixed_rate = fixed_rate
        self.notional = notional
        self.freq = 0.25

    def price(self, ois_curve):
        schedule = np.arange(self.freq, self.maturity + 1e-12, self.freq)
        pv_fixed = sum(self.fixed_rate * self.freq * ois_curve.df(time) for time in schedule)
        pv_float = 1 - ois_curve.df(self.maturity)
        return self.notional * (pv_float - pv_fixed)
