import numpy as np 
import matplotlib.pyplot as plt

# Creates a numpy array of 50 numbers from 
# 0 to 4 in steps of 0.0816
x = np.linspace(0, 4, 50)

# Plots x versus x
plt.plot(x, x, 'g.', label="x", marker='x')
# Plots x versus x^2
plt.plot(x, x**2, '-b.', label="x^2", marker='d')
# Plots x versus x^3
plt.plot(x, x**3, '--r.', label="x^3")
# Creates a plot legend
leg = plt.legend()

# Outputs the plot to screen
plt.show()