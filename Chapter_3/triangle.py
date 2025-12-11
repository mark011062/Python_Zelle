
def main():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    s = round((a+b+c)/2,2)
    area = round((s*(s-a)*(s-b)*(s-c))**0.5,2)
    print(f"The area is {area}")

main()