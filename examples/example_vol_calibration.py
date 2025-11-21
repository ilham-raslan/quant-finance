from quantfin.vol.vol_surface import VolSurface

market_options = [
    { "expiry": 1.0, "strike": 100, "market_vol": 0.2, "forward": 100 },
    { "expiry": 1.0, "strike": 105, "market_vol": 0.22, "forward": 100  },
    { "expiry": 2.0, "strike": 100, "market_vol": 0.21, "forward": 100  },
    { "expiry": 2.0, "strike": 105, "market_vol": 0.23, "forward": 100  },
]

expiry_list = [opt["expiry"] for opt in market_options]
strike_list = [opt["strike"] for opt in market_options]
market_vol_list = [opt["market_vol"] for opt in market_options]
forward_list = [opt["forward"] for opt in market_options]

vol_surface = VolSurface(expiry_list, strike_list, market_vol_list, forward_list)

vol_surface.calibrate()

print("Implied vol for T=1.5, K=102, F=100 is " + str(vol_surface.get_vol(1.5, 102, 100)))
print("Implied vol for T=1, K=100, F=100 is " + str(vol_surface.get_vol(1, 100, 100)))
print("Implied vol for T=2, K=105, F=100 is " + str(vol_surface.get_vol(2, 105, 100)))
