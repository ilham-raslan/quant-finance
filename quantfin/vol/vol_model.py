import math


class VolModel:
    def __init__(self, alpha, rho, nu):
        self.alpha = alpha
        self.rho = rho
        self.nu = nu
        self.beta = 0.5

    def get_vol(self, expiry, strike, forward):
        f = forward
        k = strike
        alpha = self.alpha
        beta = self.beta
        rho = self.rho
        nu = self.nu

        if (abs(f - k)) < 1e-12:
            fk_beta  = f ** (1 - beta)
            term_1 = alpha / fk_beta
            term_2 = (1 + (((1 - beta) ** 2) / 24) * ((alpha ** 2) / (fk_beta ** 2)) + (1 / 4) * (rho * beta * alpha * nu) / fk_beta + ((2 - 3 * rho ** 2) / 24) * nu ** 2) * expiry

            return term_1 * term_2

        logFK = math.log(f / k)
        fk = f * k
        fk_beta = fk ** ((1 - beta) / 2)

        z = (nu / alpha) * fk_beta * logFK
        x = math.log((math.sqrt(1 - 2 * rho * z + z ** 2) + z - rho) / (1 - rho))

        term_1 = alpha / (fk_beta * (1 + (((1 - beta) ** 2) / 24) * (logFK ** 2) + (((1 - beta) ** 4) / 1920) * (logFK ** 4)))
        term_2 = z / x
        term_3 = (1 + (((1 - beta) ** 2) / 24) * ((alpha ** 2) / (fk_beta ** 2)) + (1 / 4) * (rho * beta * alpha * nu) / fk_beta + ((2 - 3 * rho ** 2) / 24) * nu ** 2) * expiry

        return term_1 * term_2 * term_3
