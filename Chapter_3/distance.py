def main():
    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    y1 = int(input("Enter y1: "))
    y2 = int(input("Enter y2: "))
    distance = round(((x2-x1)**2 + (y2-y1)**2)**0.5,2)
    print(f"The distance between the two points is {distance}")

main()