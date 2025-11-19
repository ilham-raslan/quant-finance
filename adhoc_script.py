from quantfin.curves.bootstrapper import MultiCurveBootstrapper
from quantfin.curves.instruments import OISSwap, Swap3M

ois_swaps = [
    OISSwap(0.5, 0.0010),   # 6M OIS at 0.10%
    OISSwap(1.0, 0.0015),   # 1Y  OIS at 0.15%
    OISSwap(2.0, 0.0020),   # 2Y  OIS at 0.20%
    OISSwap(3.0, 0.0027),   # 3Y  OIS at 0.27%
    OISSwap(4.0, 0.0033),   # 4Y  OIS at 0.33%
    OISSwap(5.0, 0.0040)    # 5Y  OIS at 0.40%
]

swaps3m = [
    Swap3M(0.25, 0.0010),   # 3M
    Swap3M(0.50, 0.0012),   # 6M
    Swap3M(0.75, 0.0015),   # 9M
    Swap3M(1.00, 0.0030),   # 1Y
    Swap3M(1.25, 0.0035),
    Swap3M(1.50, 0.0038),
    Swap3M(1.75, 0.0039),
    Swap3M(2.00, 0.0040),   # 2Y
    Swap3M(2.25, 0.0042),
    Swap3M(2.50, 0.0045),
    Swap3M(2.75, 0.0048),
    Swap3M(3.00, 0.0050),   # 3Y
    Swap3M(3.25, 0.0053),
    Swap3M(3.50, 0.0056),
    Swap3M(3.75, 0.0060),
    Swap3M(4.00, 0.0063),   # 4Y
    Swap3M(4.25, 0.0067),
    Swap3M(4.50, 0.0070),
    Swap3M(4.75, 0.0073),
    Swap3M(5.00, 0.0075)    # 5Y
]

bootstrapper = MultiCurveBootstrapper(ois_swaps, swaps3m)
curves = bootstrapper.fit()

ois_curve = curves["ois"]
ibor3m_curve = curves["3m"]

df_1y = ois_curve.df(1.0)
print("1y ois discounting: " + str(df_1y))

zero = ois_curve.zero_rate(1.5)
print("1.5y ois zero rate: " + str(zero))

fwd = ibor3m_curve.forward_rate(1.0, 1.25)
print("1.0 to 1.25 forward rate: " + str(fwd))
