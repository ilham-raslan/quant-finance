class Interpolator:
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys

class LogLinearInterpolator(Interpolator):
    def __call__(self, x):
        i, point = 0, 0
        for i, point in enumerate(self.xs):
            if x == point:
                return self.ys[i]
            elif x > point:
                continue
            else:
                break

        return (self.ys[i - 1] ** ((self.xs[i] - x) / (self.xs[i] - self.xs[i - 1]))) * (
                    self.ys[i] ** ((x - self.xs[i - 1]) / (self.xs[i] - self.xs[i - 1])))

class LinearInterpolator(Interpolator):
    def __call__(self, x):
        pass
