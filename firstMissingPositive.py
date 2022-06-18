import numpy as np
import matplotlib.pyplot as plt

# Distance between two points


def approximate_pi_value(x, y, n):
    def Distance(x1, y1, x2, y2): return np.sqrt(((x2-x1)**2)+((y2-y1)**2))
    approximate = []
    for i in range(n-1):
        approximate.append(Distance(x[i], y[i], x[i+1], y[i+1]))
    return sum(approximate)


# Appending all possible values of pi
error_pi_values = []

x = np.linspace(-1, 1, 34)
y = np.sqrt(1-x**2)
# plt.figure(figsize=(8,5))
# plt.plot(x,y)

plt.figure(figsize=(15, 8))
g = plt.gca()
g.spines["left"].set_position(("data", 0))
g.spines["top"].set_color('none')
g.spines["right"].set_color('none')
g.spines["bottom"].set_position(("data", 0))
# Running the function
for i in range(3, 1000):
    x = np.linspace(-1, 1, i)
    y = np.sqrt(1-x**2)
    error_pi_values.append(approximate_pi_value(x, y, i))
    plt.plot(x, y)


# Approx pi value
print(error_pi_values[-1])

