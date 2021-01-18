# Import numpy package
import numpy as np

print("S121 Ajay Dilip Lingayat\n")

# Initialize two vector arrays u & v
u = np.array([3, 4, 5])
v = np.array([1, 2, 7])
print(f"u vector = {u}\nv vector = {v}")

# Take inputs for variables a & b
a = int(input("Enter value for a : "))
b = int(input("Enter value for b : "))

# Calculate 'au+bv' & dot product of a & v
d = (a*u)+(b*v)
p = np.dot(u, v)

# Display 'au+bv' & dot product of a & v
print(f"au+bv = {d}")
print(f"Dot Product of u and v = {p}")