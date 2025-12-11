#a program that computes the real roots of a quadratic equation. Program crashes if the equation has no real roots
import math

def main():
    print("This program finds the real solutions of a quadratic equation")
    print()

    a = float(input("Enter the coefficient of a: "))
    b = float(input("Enter the coefficient of b: "))
    c = float(input("Enter the coefficient of c: "))

    discRoot = math.sqrt(b*b-4*a*c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print(f"The solutions are: {root1} and {root2}")

main()


