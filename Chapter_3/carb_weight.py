def main():
    num_hyd = int(input("Enter the number of hydrogen atoms: "))
    num_car = int(input("Enter the number of carbon atoms: "))
    num_oxy = int(input("Enter the number of oxygen atoms: "))

    molecular_weight = num_hyd * 1.00794 + num_car * 12.0107 + num_oxy * 15.9994

    print(f"The molecular weight is {molecular_weight}")

main()