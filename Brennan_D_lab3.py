# Daniel Brennan
# Section 24
# Version 1.0 Lab 3
# 5/20/2025

# Notes: I used sympy instead of numpy to do the matrix operations. It has a lot of functionality in regards to matrixes and sympbolic math opretations.
# I also used sympy to print the matrices in a more readable format.
# I will discuss the functions I used in the comments below.
# Running the code and receiving the output is the best way to see the calculations.
# pprint() is used to print the matrix in a more readable format throughout the code

from sympy import *
# 0---------------------------------------------
A = Matrix([[2, 0, 0, 1, 3], [-2, 0, 1, 2, -2], [-5, 0, 0, -3, 4], [7, 1, 0, 5, -1], [2, 1, 4, 9, 6]])
b = Matrix([8, 7, -6, 5, 3])
print("Matrix A is: \n")
pprint(A)
print("b is: \n")
pprint(b)
# 1
print(" # 1 ---------------------------------------------------------")
matrixDet = A.det() # matrixDet = 116 .det() returns the determinant of the matrix
print(f"The determinant of A is {matrixDet}")
if matrixDet != 0: # not zero it is invertible
    print("The matrix is invertible because the det isnt 0.")
    oneOverDet = (1/matrixDet)
    detMatrixInverse = A.inv().det()
    print()
    print("1/det(A) is \n", oneOverDet)
    print("det(A^-1) is \n", detMatrixInverse)
    if (detMatrixInverse == oneOverDet):  # 1/116 = 1/116
        print("The determinant of the inverse is equal to 1/det(A).")
else:
    print("The matrix is not invertible.")
# 2
print(" # 2 ---------------------------------------------------------")
B = A.applyfunc(lambda x: x + 1) # A.applyfunc() applies a function to each element of the matrix, 
# lamba creates a short unnamed function that is then used on each element "x" where x is the input from element and becomes the output
AB = A * B
detAB = AB.det()
detAdetB = A.det() * B.det()
if detAB == detAdetB:
    print("det(AB) = det(A) * det(B)")
    print(f"det(AB) is {detAB}")
    print(f"det(A) * det(B) is {detAdetB}")
else:
    print("det(AB) is not = det(A) * det(B)")
# 3
print(" # 3 ---------------------------------------------------------")
AAinv = A * A.inv() # A.inv() returns the inverse of the matrix as matrix
AinvA = A.inv() * A
I = eye(A.shape[0]) # eye() creates an identity matrix of the same size as A, it is sympy's version of np.indentity()
# A.shape[0] returns the number of rows in A "0" is the first element of the tuple
if AAinv == I and AinvA == I:
    print("A * A^-1 = I and A^-1 * A = I")
    print("Identity matrix is: \n")
    pprint(I)
    print("A * A^-1 is: \n")
    pprint(AAinv)
    print(f"A^-1 * A is: \n")
    pprint(AinvA)

# 4
print(" # 4 ---------------------------------------------------------")
I = eye(A.shape[0])
AI = A.row_join(I)
print(f"AI is: \n")
pprint(AI)

AIrref = AI.rref()[0]
print("AI RREF is: \n")
pprint(AIrref)
IAinv = I.row_join(A.inv()) # I.row_join(A.inv) joins the identity matrix with the inverse of A 
# so it adds the columns of the inverse of A to back of the identity matrix
print("IA^-1 is: \n")
pprint(IAinv)

if (AIrref == IAinv):
    print("AI RREF = IA^-1")
# 4i
print( " # 4i ---------------------------------------------------------")
Ainv = AIrref[:, 5:]
if (I == (Ainv * A)):
    print("A^-1 * A = I: \n")
    pprint(Ainv * A)


# 5#
print(" # 5 ---------------------------------------------------------")
AAugmented = A.row_join(b)
AAugmentedRREF = AAugmented.rref()[0]
print("A Augmented is \n")
pprint(AAugmented)
print("A Augmented RREF is \n")
pprint(AAugmentedRREF)
x0, x1, x2, x3, x4, x5 = symbols('x:6') # creates the sympy symbol type for variables x0-x5, each symbol holds x0, x1, ect..
# symbols can be manipulated algebricly and used in equations and matrix calculations

xMatrix = Matrix([x1, x2, x3, x4, x5]) # not using x0 symbol
xSols = AAugmentedRREF[:, 5:]
print("The soloutions using RREF are: \n")
eq = Eq(xMatrix, xSols)
pprint(eq)

#6
print(" # 6 ---------------------------------------------------------")
cramersSols = Matrix.zeros(5, 1) # creates a matrix of 0s for the soloutions
for i in range(5):
    Areplaced = A.copy() # copies A to Areplaced
    Areplaced[:, i] = b
    (Areplaced.det())/(A.det())
    cramersSols[i, 0] = (Areplaced.det())/(A.det())
print("The solutions using Cramers rule are: \n")
eq_cramers = Eq(xMatrix, cramersSols)
pprint(eq_cramers)

if (xSols == cramersSols):
    print("The solutions obtained using RREF and Cramer's rule are equal.")