import random
import pylab

import scipy.integrate


def gaussian(x, mu, sigma):
    factor1 = 1.0 / sigma * ((2 * pylab.pi) ** 0.5)
    factor2 = pylab.e ** -(((x - mu) ** 2) / (2 * sigma ** 2))
    return factor1 * factor2


def check_empirical(num_trials):
    for t in range(num_trials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu =', mu, 'and sigma =', sigma)

        for num_std in (1, 1.96, 3):
            area = scipy.integrate.quad(gaussian, mu - num_std * sigma, mu + num_std * sigma, (mu, sigma))[0]
            print('Fraction within', num_std, 'std =', round(area, 4))


check_empirical(3)
