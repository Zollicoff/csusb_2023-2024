import numpy as np

# Define the function
def f(x):
    return 5 / (x + 1)**3

# Interval [a, b] and number of subintervals n
a, b = 0, 6
n = 2
delta_x = (b - a) / n

# X-values for LHS, RHS, MID, and Trap
x_lhs = np.linspace(a, b - delta_x, n)
x_rhs = np.linspace(a + delta_x, b, n)
x_mid = np.linspace(a + delta_x/2, b - delta_x/2, n)

# Calculate LHS
LHS = np.sum(f(x_lhs)) * delta_x

# Calculate RHS
RHS = np.sum(f(x_rhs)) * delta_x

# Calculate Trapezoidal Rule
Trap = np.sum(f(x_lhs) + f(x_rhs)) * delta_x/2

# Calculate Midpoint Rule
MID = np.sum(f(x_mid)) * delta_x

Print(LHS, RHS, Trap, MID)
