Task 1:
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


Task 2:
fn=input("Enter Filename: ")
f = fn.split(".")
print ("Extension of the file is : " + f[-1])
