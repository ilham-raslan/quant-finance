import pytest
from quantfin.vol.vol_surface import VolSurface
from quantfin.vol.vol_calibrator import VolCalibrator

def test_vol_surface_add_get():
    surface = VolSurface()
    surface.add_market_vol(expiry=1.0, strike=100, vol=0.2)
    surface.interpolate()
    vol = surface.get_vol(expiry=1.0, strike=100)
    assert vol == pytest.approx(0.2)

def test_equity_calibrator_init():
    surface = VolSurface()
    calibrator = VolCalibrator(surface)
    assert calibrator.vol_surface == surface
