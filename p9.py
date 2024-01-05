from math import ceil
import numpy as np
from scipy import linalg
import pylab as pl

# LOWESS function - Locally Weighted Scatterplot Smoothing
def lowess(x, y, f=2. / 3., iter=3):
    n = len(x)
    r = int(ceil(f * n))  # Computing the number of neighbours
    h = [np.sort(np.abs(x - x[i]))[r] for i in range(n)]  # Bandwidth for each x

    # Weight matrix
    w = np.clip(np.abs((x[:, None] - x[None, :]) / h), 0.0, 1.0)
    w = (1 - w ** 3) ** 3

    yest = np.zeros(n)
    delta = np.ones(n)

    # Iteratively updating weights and regression estimates
    for iteration in range(iter):
        for i in range(n):
            weights = delta * w[:, i]
            b = np.array([np.sum(weights * y), np.sum(weights * y * x)])
            A = np.array([[np.sum(weights), np.sum(weights * x)],
                          [np.sum(weights * x), np.sum(weights * x * x)]])
            beta = linalg.solve(A, b)
            yest[i] = beta[0] + beta[1] * x[i]

        residuals = y - yest
        s = np.median(np.abs(residuals))
        delta = np.clip(residuals / (6.0 * s), -1, 1)
        delta = (1 - delta ** 2) ** 2

    return yest

# Main block to test LOWESS
if __name__ == '__main__':
    # Generating test data
    n = 100
    x = np.linspace(0, 2 * np.pi, n)  # Periodic data
    y = np.sin(x) + 0.3 * np.random.randn(n)  # Sine wave with noise

    # Fraction of data points used to compute each y-value in yest
    f = 0.25

    # Applying LOWESS
    yest = lowess(x, y, f, 3)

    # Plotting the data and the LOWESS approximation
    pl.clf()
    pl.plot(x, y, label='y noisy')
    pl.plot(x, yest, label='y predicted')
    pl.legend()
    pl.show()
