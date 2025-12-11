import math

def main():
    radius = float(input("Enter the radius of the sphere: "))
    volume = (4/3) * math.pi * (radius**3)
    surf_area = 4 * math.pi * radius**2

    print(f"The volume of the sphere is {volume}")
    print(f"The surface area of the sphere is {surf_area}")


main()