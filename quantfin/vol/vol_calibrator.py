import numpy as np
from scipy.optimize import least_squares

from quantfin.vol.vol_model import VolModel


class VolCalibrator:
    """Generic VolCalibrator class"""

    def __init__(self, expiries, strikes, market_vols, forwards):
        self.expiries = expiries
        self.strikes = strikes
        self.market_vols = market_vols
        self.forwards = forwards

    def residuals(self, params, expiries, strikes, forwards, market_vols):
        alpha, rho, nu = params
        model = VolModel(alpha, rho, nu)

        return np.array([
            model.get_vol(T, K, F) - market_vol
            for T, K, F, market_vol in zip(expiries, strikes, forwards, market_vols)
        ])

    def calibrate(self):
        expiries = np.array(self.expiries)
        strikes = np.array(self.strikes)
        forwards = np.array(self.forwards)
        market_vols = np.array(self.market_vols)

        # initial guesses
        x0 = np.array([0.2, -0.2, 0.5])

        lower = [1e-8, -0.999, 1e-8]
        upper = [10.0, 0.999, 5.0]

        result = least_squares(
            fun=self.residuals,
            x0=x0,
            bounds=(lower, upper),
            args=(expiries, strikes, forwards, market_vols),
            method='trf',
            verbose=2
        )

        alpha_fit, rho_fit, nu_fit = result.x
        return VolModel(alpha_fit, rho_fit, nu_fit)
