#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    x = x[:, np.newaxis]
    model = LinearRegression(fit_intercept=True)
    model.fit(x, y)

    xfit = np.linspace(0, 10, 20)[:,np.newaxis]
    yfit = model.predict(xfit)

    return model.coef_[0], model.intercept_
    
def main():
    n = 20
    x = np.linspace(0, 10, n)
    y = x**2 + 2 * np.random.randn(n)
    coef, intercept = fit_line(x, y)

    print(f"Slope: {coef}")
    print(f"Intercept: {intercept}")

    yfit = coef*x + intercept
    plt.plot(x, y, 'o')
    plt.plot(x, yfit)
    plt.show()


if __name__ == "__main__":
    main()
