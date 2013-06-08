"""
sincos/CalAndDraw.py
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def CD(argument):
    plt.figure()
    k = float(argument.k)
    A = float(argument.A)
    phy = float(argument.phy)
    x = np.linspace(argument.x_min, argument.x_max, 10000)
    y = np.sin(k * x + phy) * A
    z = np.cos(k * x**2 - phy) * A / 2.0
    plt.plot(x, y, label="$Asin(kx+phy)$", color="red", linewidth=2)
    plt.plot(x, z, "b--", label="$\\frac{A}{2}cos(kx^2-phy)$")
    plt.ylim(-A, A)
    plt.grid()
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig('sincos/images/test'+str(argument.id)+'.png')
    return