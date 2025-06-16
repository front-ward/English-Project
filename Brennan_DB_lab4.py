import matplotlib.pyplot as plt
import numpy as np
from sympy import *
# 1---------------------------

def trans(dx, dy):

    return Matrix([
        [1, 0, dx],
        [0, 1, dy],
        [0, 0, 1]
    ])

# Required test
T = trans(5, -5.2)
point = Matrix([1, 1, 1])
result = T * point

print("Result of cell 1")
print(result)

# 2---------------------------

def rot(ang_deg):
    angle_rad = ang_deg * pi / 180  
    return Matrix([
        [cos(angle_rad), -sin(angle_rad), 0],
        [sin(angle_rad),  cos(angle_rad), 0],
        [0,               0,              1]
    ])


R = rot(-45)
point = Matrix([1, 0, 1])
result = R * point

print("cell 2")
print(result.evalf(4)) 

# 3---------------------------


p = Matrix([5, 0, 1])

plt.plot(p[0], p[1], 'r*')  # red star at (5, 0)

for angle in range(5, 360, 5):
    p_rotated = rot(angle) * p
    x = float(p_rotated[0])
    y = float(p_rotated[1])
    plt.plot(x, y, 'k*') 


plt.axis('square')
plt.title('circle by rot(d) radius 5')
plt.xlabel('x coord')
plt.ylabel('y coord')
plt.grid(True)

plt.show()
# 4---------------------------

x_coords = np.array([[5, 8, 8, 5]])   # x-coordinates
y_coords = np.array([[0, 0, 1, 1]])   # y-coordinates
z_coords = np.array([[1, 1, 1, 1]])   # homogeneous coordinate w = 1

rectf = np.concatenate((x_coords, y_coords, z_coords), axis=0)

plt.figure(2)
plt.fill(rectf[0, :], rectf[1, :], facecolor='b')  
plt.axis('square')
plt.axis([-10, 10, -10, 10])
plt.title('rectangle')
plt.show()
# 5---------------------------

rectf_sym = Matrix(rectf)

T1 = trans(10, 0)
rectf_10x = T1 * rectf_sym

T2 = trans(0, 5)
rectf_10x_5y = T2 * rectf_10x

plt.figure(3)
plt.fill(rectf[0, :], rectf[1, :], 'b', label='Original')  
plt.fill([float(x) for x in rectf_10x[0, :]], [float(y) for y in rectf_10x[1, :]], 'r', label='Translated +10x')  
plt.fill([float(x) for x in rectf_10x_5y[0, :]], [float(y) for y in rectf_10x_5y[1, :]], 'g', label='Translated +10x +5y')  

plt.axis('square')
plt.axis([-10, 25, -10, 20])
plt.title('Translation of Rectangle')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# 6---------------------------

x_coords = np.array([[5, 8, 8, 5]])
y_coords = np.array([[0, 0, 1, 1]])
z_coords = np.array([[1, 1, 1, 1]])
rectf = np.concatenate((x_coords, y_coords, z_coords), axis=0)
rectf_sym = Matrix(rectf)

plt.figure(4)

for angle in range(0, 360, 20):
    R = rot(angle)
    rotated_rect = R * rectf_sym

    x_vals = [float(x) for x in rotated_rect[0, :]]
    y_vals = [float(y) for y in rotated_rect[1, :]]

    color = 'r' if angle == 0 else 'b'
    plt.fill(x_vals, y_vals, facecolor=color)

plt.axis('square')
plt.axis([-10, 10, -10, 10])
plt.title('rotated rectangle')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
# 7---------------------------

x_coords = np.array([[-1,  1, 1, -1]])
y_coords = np.array([[-1, -1, 1,  1]])
z_coords = np.array([[ 1,  1, 1,  1]])  # homogeneous coordinates

square = np.concatenate((x_coords, y_coords, z_coords), axis=0)
square_sym = Matrix(square)

# Rotate 30 degrees
square_rotated = rot(30) * square_sym

# Plot original square (blue)
plt.figure(5)
plt.fill(square[0, :], square[1, :], facecolor='b', label='Original')

# Plot rotated square (green)
x_rot = [float(x) for x in square_rotated[0, :]]
y_rot = [float(y) for y in square_rotated[1, :]]
plt.fill(x_rot, y_rot, facecolor='g', label='Rotated 30°')

# Formatting
plt.axis('square')
plt.axis([-3, 3, -3, 3])
plt.title('Square and Rotated Square')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
# 8---------------------------
# Original rectangle (from part 4)
x_coords = np.array([[5, 8, 8, 5]])
y_coords = np.array([[0, 0, 1, 1]])
z_coords = np.array([[1, 1, 1, 1]])
rectf = np.concatenate((x_coords, y_coords, z_coords), axis=0)
rectf_sym = Matrix(rectf)

# ----------------------------
# First rotation about point (8, 1)
pivot1 = (8, 1)
T_to_origin1 = trans(-pivot1[0], -pivot1[1])
T_back1 = trans(pivot1[0], pivot1[1])
R = rot(120)
rotated1 = T_back1 * R * T_to_origin1 * rectf_sym

# ----------------------------
# Second rotation about point (5, 1)
pivot2 = (5, 1)
T_to_origin2 = trans(-pivot2[0], -pivot2[1])
T_back2 = trans(pivot2[0], pivot2[1])
rotated2 = T_back2 * R * T_to_origin2 * rectf_sym

# ----------------------------
# Plot all 3 rectangles
plt.figure(6)

# Original rectangle (blue)
plt.fill(rectf[0, :], rectf[1, :], facecolor='blue', label='Original')

# Rotated about (8,1) – orange
x1 = [float(val) for val in rotated1[0, :]]
y1 = [float(val) for val in rotated1[1, :]]
plt.fill(x1, y1, facecolor='orange', label='Rotated about (8,1)')

# Rotated about (5,1) – green
x2 = [float(val) for val in rotated2[0, :]]
y2 = [float(val) for val in rotated2[1, :]]
plt.fill(x2, y2, facecolor='green', label='Rotated about (5,1)')

# Format plot
plt.axis('square')
plt.axis([0, 20, -5, 15])  
plt.title('Rectangle Rotated About Arbitrary Points')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()