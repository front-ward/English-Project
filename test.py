import numpy as np
from sympy import *

# Part 4/Cell 4
def get_solution(t):
    return np.array([
        [-3 - t],
        [2 + (2 * t)],
        [t]
    ])

# Part 1/Cell 1
A = Matrix([[1, 2, -3], [2, 5, -8], [3, 8, -13]])
B = Matrix([[1], [4], [7]])
augAB = BlockMatrix([[A, B]]).as_explicit()
AB = np.array(augAB)
print("Augmented Matrix: ")
print(AB)

# Part 2/Cell 2
rrefAB = augAB.rref()
print("RREF Matrix: ")
print(rrefAB)  # pivot at (1,1) and (2,2), x1 and x2 are basic variables, x3 is a free variable

# Part 3/Cell 3
# solution:
# x1 + x3 = -3
# x2 - 2x3 = 2
# x3 = real nums

# Part 5/Cell 5
t_values = [1, -4]
for t in t_values:
    print("-" * 30)
    sol_vec = get_solution(t)
    result = A @ sol_vec  # A * solution
    print(f"t = {t}")
    print("Solution vector: \n", sol_vec)
    print("Result: \n", result)
    print("Solution for comparison: \n", B)
    print("Are the results equal: ", np.array_equal(np.array(result), np.array(B)))
    print("-" * 30)

# Part 6/Cell 6 needs comments
A1_R1 = AB[0:1]  # Creates an array for row 1 of the augmented matrix
A1_R2 = AB[1:2]  # Creates an array for row 2 of the augmented matrix
A1_R3 = AB[2:3]  # Creates an array for row 3 of the augmented matrix
A1_R2 = A1_R2 - 2 * A1_R1  # Row 2 = row 2 - 2(Row 1)
A1_R3 = A1_R3 - 3 * A1_R1  # Row 3 = row 3 - 3(Row 1)
A2 = np.concatenate((A1_R1, A1_R2, A1_R3), axis=0)  # Creates the new matrix with reduced rows
print("Reduced matrix: ")
print(A2)

A2_R1 = A2[0:1]  # Creates a new array for row 1 of the augmented matrix
A2_R2 = A2[1:2]  # Creates a new array for row 2 of the augmented matrix
A2_R3 = A2[2:3]  # Creates a new array for row 3 of the augmented matrix
A2_R1 = A2_R1 - 2 * A2_R2  # Row 1 = Row 1 - 2(Row 2)
A2_R3 = A2_R3 - 2 * A2_R2  # Row 3 = Row 3 - 2(Row 2)
A3 = np.concatenate((A2_R1, A2_R2, A2_R3), axis=0)  # Creates the new matrix with reduced rows
print("RREF matrix: ")
print(A3)  # Prints the RREF matrix as an array
