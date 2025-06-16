import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# Generate a range of k values between 0.05 and 6.90
k_values = np.linspace(0.05, 6.90, 100)  # 100 points between 0.05 and 6.90

x1_list = []
x2_list = []
x3_list = []

# Iterate over the range of k values
for k in k_values:
    AugmentedMatrix = Matrix([[k, 0, -16, -9], [-3, 1, 4, 2], [2, -3, 4, 4]])
    rref = AugmentedMatrix.rref()
    rref_array = np.array(rref[0].tolist(), dtype=float)
    x1_list.append(rref_array[0, 3])
    x2_list.append(rref_array[1, 3])
    x3_list.append(rref_array[2, 3])

# Plotting
plt.figure(figsize=(10, 8))
plt.plot(k_values, x1_list, label='x1', color='blue')
plt.plot(k_values, x2_list, label='x2', color='orange')
plt.plot(k_values, x3_list, label='x3', color='green')
plt.xlabel('k')
plt.ylabel('variables x1, x2, x3')
plt.title('Solution of linear equations vs k: Full Range')
plt.grid(True)
plt.legend()
plt.show()
