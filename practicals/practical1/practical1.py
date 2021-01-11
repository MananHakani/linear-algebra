"""
   Python program to understand and plot complex numbers
"""

print("Linear Algebra Practical No.1\n\
    S121 Ajay Dilip Lingayat\n")

#Initializing complex numbers - x & y
x, y = 1+3j, 2+3j
print(f"Addition of two complex numbers = {x+y}")

#Conjugate of complex number
a=4+2j
print(f"Conjugate of a given complex number = {a.conjugate()}")


#library for plotting graphs
import matplotlib.pyplot as plt

#complex numbers
a=[-2+4j, -1.5+3j, -1+5j, 0+2j, 1+1.5j]

#sorting real and imaginary numbers
X=[x.real for x in a]
Y=[y.imag for y in a]

"""plotting graph using scatter() method\
   and displaying it by calling show() method."""
plt.scatter(X, Y, color="blue")
plt.show()


"""
    ## Extra Activities

    1. (1+3j) + (10+20j)
    2. If x=1+3j then find (x-1)**2
    3. 1+2j*3
    4. 4*3j**2
    5. If x=1+3j then find x.real & x.imag
    6. If x=1+3j then find x.conjugate
    7. Plot S = {3+3i, 4+3i, 2+i, 2.5+i, 3+i, 3.25+i}
"""
print("\n~~~ Extra Activities ~~~\n")

#Activity no.1
addition = (1+3j) + (10+20j)
print(f"Addition of (1+3j) + (10+20j) = {addition}")

#Activity no.2
x=1+3j
if x == 1+3j:
    print(f"If x=1+3j then (x-1)**2 = {(x-1)**2}")

#Activity no.3
print(f"1+2j**3 = {1+2j**3}")

#Activity no.4
print(f"4*3j**2 = {4*3j**2}")

#Activity no.5
x=1+3j
print(f"If x=1+3j then x.real = {x.real}, x.imag = {x.imag}")

#Activity no.6
x=1+3j
print(f"If x=1+3j then x.conjugate = {x.conjugate()}")

#Activity no.7
S=[3+3j, 4+3j, 2+1j, 2.5+1j, 3+1j, 3.25+1j]

X=[x.real for x in S]
Y=[y.imag for y in S]

plt.scatter(X, Y, color="orange")
plt.show()