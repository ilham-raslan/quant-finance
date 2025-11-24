from examples.data.markets import OIS_FUTURES, OIS_SWAPS, SWAPS_3M
from quantfin.bootstrap.bootstrapper import MultiCurveBootstrapper

ois_futures = OIS_FUTURES
ois_swaps = OIS_SWAPS
swaps_3m = SWAPS_3M

ois_instruments = ois_futures + ois_swaps

bootstrapper = MultiCurveBootstrapper(ois_instruments, swaps_3m)
curves = bootstrapper.fit()

ois_curve = curves["ois"]
ibor3m_curve = curves["3m"]

df_1y = ois_curve.df(1.0)
print("1y ois discounting: " + str(df_1y))

zero = ois_curve.zero_rate(1.5)
print("1.5y ois zero rate: " + str(zero))

fwd = ibor3m_curve.forward_rate(1.0, 1.25)
print("1.0 to 1.25 forward rate: " + str(fwd))

ois_curve.plot_dfs()
ibor3m_curve.plot_forward_rates()
