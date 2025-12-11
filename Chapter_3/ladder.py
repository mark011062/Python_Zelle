import math

def main():
    height = float(input("Enter the height of the house (in feet) "))
    angle_degrees = float(input("Enter the angle in degrees "))
    angle = (math.pi/180)*angle_degrees
    length = round(height/math.sin(angle),1)
    print(f"The length of the ladder needs to be {length} feet")

main()