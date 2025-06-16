import sympy as sp


X = sp.Matrix([[3], [4], [5]])    
Y = sp.Matrix([[10], [13], [14]]) 


beta1_expr = (X.T * X).inv() * X.T * Y


beta1_value = beta1_expr[0]


x_val = 21
y_prediction = beta1_value * x_val


print("(1) Beta_1 =", beta1_value)
print("(2) Beta_1 = (Xᵀ X)^(-1) Xᵀ Y =", beta1_expr)
print("(3) y(21) =", y_prediction)