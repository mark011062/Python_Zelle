#Program to convert kilos to miles

def kilos_to_miles():
    kilos = float(input("Enter the distance in kilometers: "))
    k_to_m = kilos * 0.62
    print(f"{kilos} is equal to {k_to_m} miles")

kilos_to_miles()

quit = input("Press <ENTER> to quit")