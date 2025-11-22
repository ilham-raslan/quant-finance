from quantfin.vol.caplet3m_vol_calibrator import Caplet3MVolCalibrator


class Caplet3MVolSurface:
    """Represents a volatility surface for 3m caplets: vol = f(strike, expiry)"""

    def __init__(self, caplets = None, ibor_curve = None):
        self.caplets = caplets if caplets is not None else []
        self.ibor_curve = ibor_curve
        self.model = None

    def add_caplet(self, caplet):
        self.caplets.append(caplet)

    def calibrate(self):
        calibrator = Caplet3MVolCalibrator(self.caplets, self.ibor_curve)
        self.model = calibrator.calibrate()

    def get_vol(self, expiry, strike, forward):
        """Return interpolated vol for a given expiry/strike"""
        if self.model is not None:
            return self.model.get_vol(expiry, strike, forward)
        else:
            raise Exception("Model is not yet calibrated, run calibrate() first")
