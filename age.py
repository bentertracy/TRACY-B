# Program to calculate Area, Perimeter, and Volume of various shapes
# No imports used

def rectangle():
    l = float(input("Enter length of rectangle: "))
    w = float(input("Enter width of rectangle: "))
    area = l * w
    perimeter = 2 * (l + w)
    print(f"Area = {area}")
    print(f"Perimeter = {perimeter}")

def square():
    s = float(input("Enter side of square: "))
    area = s * s
    perimeter = 4 * s
    print(f"Area = {area}")
    print(f"Perimeter = {perimeter}")

def circle():
    r = float(input("Enter radius of circle: "))
    pi = 3.1416   # Approximation since no import
    area = pi * r * r
    perimeter = 2 * pi * r
    print(f"Area = {area}")
    print(f"Circumference = {perimeter}")

def cube():
    a = float(input("Enter side of cube: "))
    volume = a ** 3
    surface_area = 6 * (a ** 2)
    print(f"Volume = {volume}")
    print(f"Surface Area = {surface_area}")

def cuboid():
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    volume = l * w * h
    surface_area = 2 * (l*w + l*h + w*h)
    print(f"Volume = {volume}")
    print(f"Surface Area = {surface_area}")

def sphere():
    r = float(input("Enter radius: "))
    pi = 3.1416
    volume = (4/3) * pi * (r ** 3)
    surface_area = 4 * pi * (r ** 2)
    print(f"Volume = {volume}")
    print(f"Surface Area = {surface_area}")

# Menu
while True:
    print("\n--- Shape Calculator ---")
    print("1. Rectangle (Area & Perimeter)")
    print("2. Square (Area & Perimeter)")
    print("3. Circle (Area & Circumference)")
    print("4. Cube (Volume & Surface Area)")
    print("5. Cuboid (Volume & Surface Area)")
    print("6. Sphere (Volume & Surface Area)")
    print("7. Exit")

    choice = input("Choose a shape (1-7): ")

    if choice == "1":
        rectangle()
    elif choice == "2":
        square()
    elif choice == "3":
        circle()
    elif choice == "4":
        cube()
    elif choice == "5":
        cuboid()
    elif choice == "6":
        sphere()
    elif choice == "7":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")