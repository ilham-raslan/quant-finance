from quantfin.bootstrap.interpolation import LogLinearInterpolator


class IBORCurve3M:
    def __init__(self, ois_curve):
        self.times = [0]
        self.dfs = [1]

    def add_knot(self, t, df):
        self.times.append(t)
        self.dfs.append(df)

    def df(self, t):
        interpolator = LogLinearInterpolator(self.times, self.dfs)
        return interpolator(t)

    def forward_rate(self, t1, t2):
        return (self.df(t1) / self.df(t2) - 1) / 0.25
