from math import sqrt
a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input ("Value of c:"))
delta_square = b**2 - 4 * a * c
delta = sqrt(delta_square)
root1 = (-b + delta) / (2 * a) 
root2= (-b - delta) / (2 * a)

print(f"The roots are {root1} and {root2}")