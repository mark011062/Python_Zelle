def main():
    seconds_passed = float(input("Enter the number of seconds since the lightening strike and the sound of thunder: "))
    distance = (seconds_passed * 1100)/5280
    print(f"The lightening is {distance} miles away")

main()

