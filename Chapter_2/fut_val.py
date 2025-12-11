#A program to compute the value of an investment carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of an investment")

    num_years = int(input("Enter the number of years for the investment: "))
    principal = float(input("Enter the intial principal: "))
    apr = float(input("Enter the annual interest rate: "))
    yearly_con = float(input("Enter the yearly contribution: "))

    for _ in range(num_years):
        principal = principal * (1+apr)
        principal += yearly_con

    print(f"The value in {num_years} years is {principal} ")

main()