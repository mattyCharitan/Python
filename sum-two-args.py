import sys
import datetime
import math

if len(sys.argv) >= 3:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
else:
    x = float(input("Enter a value for x: "))
    y = float(input("Enter a value for y: "))

print(x + y)

# Print the current date and time
print(datetime.datetime.now())

# Ask the user for the radius of the circle and compute its area
r = float(input("Enter the radius of the circle: "))
A = math.pi * r**2
print("The area of the circle is:", A)
