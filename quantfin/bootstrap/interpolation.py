class Interpolator:
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys

class LogLinearInterpolator(Interpolator):
    def __call__(self, x):
        # error out for now if we interpolate a date past the last knot
        if x > self.xs[-1]:
            raise Exception("Interpolation date is past final knot, this is not yet supported")

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
