import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# Part 1: Single value at k = 7
k = 7
AugmentedMatrix = Matrix([[k, 0, -16, -9], [-3, 1, 4, 2], [2, -3, 4, 4]])
rref = AugmentedMatrix.rref()
rref_array = np.array(rref[0].tolist(), dtype=float)
print("RREF at k=7:\n", rref_array)
# # RREF at k=7:
#  [[ 1.          0.         -2.28571429  0.        ]
#  [ 0.          1.         -2.85714286  0.        ]
#  [ 0.          0.          0.          1.        ]]
# The third row simplifies to 0=1, indicating an inconsistent system with no solution.

# Part 2: test values
k = np.arange(4, 6.95, 0.05) #arrange addresses the 4:0.05:6.90 syntax, lists those values in k
i = 0 # indexing variable
results = np.zeros((3, len(k)))
for w in k: # Iterate over the selected k values, w unpacks the values in k
    AugmentedMatrix = Matrix([[w, 0, -16, -9], [-3, 1, 4, 2], [2, -3, 4, 4]])
    rref = AugmentedMatrix.rref()
    rref_array = np.array(rref[0].tolist(), dtype=float) # Convert to numpy array for easier manipulation
    results[:, i] = rref_array[:, 3] # Extract the last column of the RREF matrix, which contains the solutions and adds it to the indexed column of the loop
    i += 1 # Increment the index for the next k value

# Part 3

#list for each soloution of x1 x2 and x3
x1_list = results[0, :].tolist()
x2_list = results[1, :].tolist()
x3_list = results[2, :].tolist()

# Iterate over the range of k values

# Plotting
plt.figure(figsize=(10, 8))
plt.plot(k, x1_list, label='x1', color='blue')
plt.plot(k, x2_list, label='x2', color='orange')
plt.plot(k, x3_list, label='x3', color='green')
plt.xlabel('k')
plt.ylabel('variables x1, x2, x3')
plt.title('Solution of linear equations vs k: Full Range')
plt.grid(True)
plt.legend()
plt.show()
#As k approaches 7, the graph shows that the solution variables x1, x2, and x3 ​diverge, indicating that the system becomes unstable and cannot be solved reliably at that point. 
# This behavior is confirmed by the RREF of the augmented matrix at k=7, which reveals an inconsistent system—specifically, a row reduces to 0=1, meaning no solution exists. 
#  at k=7, the coefficient matrix becomes singular, and the system has no valid solution