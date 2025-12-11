import math
def main():
    diameter = float(input("Enter the diameter of the pizza: "))
    cost = float(input("Enter the cost of the pizza: "))

    area = math.pi * (diameter/2)**2
    cost_per_inch = cost/area
    print(f"The area of the pizza is: {area}")
    print(f"The cost per square inch of the pizza is {cost_per_inch}")

main()