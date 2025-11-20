import numpy as np

class Swap3M:
    def __init__(self, maturity, fixed_rate, notional=1.0):
        self.maturity = maturity
        self.fixed_rate = fixed_rate
        self.notional = notional
        self.freq = 0.25

    def price(self, ois_curve, curve3m):
        schedule = np.arange(self.freq, self.maturity + 1e-12, self.freq)
        pv_fixed = sum(self.fixed_rate * self.freq * ois_curve.df(time) for time in schedule)
        pv_float = sum(curve3m.forward_rate(time - self.freq, time) * self.freq * ois_curve.df(time) for time in schedule)
        return self.notional * (pv_float - pv_fixed)
