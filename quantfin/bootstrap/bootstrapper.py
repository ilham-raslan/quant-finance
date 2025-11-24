import numpy as np

from quantfin.curves.ibor_curve import IBORCurve3M
from quantfin.curves.ois_curve import OISCurve
from quantfin.instruments.ois_future import OISFuture
from quantfin.instruments.ois_swap import OISSwap


class MultiCurveBootstrapper:
    def __init__(self, ois_instruments, swaps3m):
        self.ois_instruments = ois_instruments
        self.swaps3m = swaps3m

    def bootstrap_ois(self):
        ois_curve = OISCurve()

        for i, instrument in enumerate(self.ois_instruments):
            if isinstance(instrument, OISFuture):
                df = ois_curve.df(instrument.maturity - instrument.accrual) / (1 + instrument.accrual * instrument.market_rate())
                ois_curve.add_knot(instrument.maturity, df)
            elif isinstance(instrument, OISSwap):
                schedule = np.arange(instrument.freq, instrument.maturity + 1e-12, instrument.freq)
                k = sum(instrument.freq * instrument.fixed_rate * ois_curve.df(t) for t in schedule[:-1])
                df = (1 - k) / (instrument.freq * instrument.fixed_rate + 1)
                ois_curve.add_knot(instrument.maturity, df)
            else:
                raise Exception("Instrument " + instrument.__class__.__name__ + " is not supported for OIS bootstrapping")

        return ois_curve

    def bootstrap_ibor3m(self, ois_curve):
        ibor3m_curve = IBORCurve3M(ois_curve)
        for i, swap in enumerate(self.swaps3m):
            schedule = np.arange(0.25, swap.maturity + 1e-12, 0.25)
            fixed_leg_pv = swap.fixed_rate * sum(0.25 * ois_curve.df(time) for time in schedule)
            k = sum(ois_curve.df(time) * ibor3m_curve.forward_rate(time - 0.25, time) * 0.25 for time in schedule[:-1])

            df = ibor3m_curve.df(swap.maturity - 0.25) * ois_curve.df(swap.maturity) / (ois_curve.df(swap.maturity) + fixed_leg_pv - k)

            ibor3m_curve.add_knot(swap.maturity, df)

        return ibor3m_curve

    def fit(self):
        ois_curve = self.bootstrap_ois()
        ibor_3m_curve = self.bootstrap_ibor3m(ois_curve)

        return {
            "ois" : ois_curve,
            "3m" : ibor_3m_curve
        }
