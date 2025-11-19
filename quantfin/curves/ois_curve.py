import math

from quantfin.bootstrap.interpolation import LogLinearInterpolator

class OISCurve:
    def __init__(self):
        self.times = [0]
        self.dfs = [1]

    def add_knot(self, t, df):
        self.times.append(t)
        self.dfs.append(df)

    def df(self, t):
        interpolator = LogLinearInterpolator(self.times, self.dfs)
        return interpolator(t)

    def zero_rate(self, t):
        return -1 * math.log(self.df(t)) / t
