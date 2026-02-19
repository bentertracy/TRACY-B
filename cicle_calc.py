# circle_calc.py
import math
def circle_area(radius):
    return math.pi * radius ** 2
# Main program
radius = float(input("Enter the radius of the circle: "))
area = circle_area(radius)
print(f"The area of the circle is {area:.2f}")