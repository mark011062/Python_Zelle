
def main():
    amount = int(input("How many numbers would you like to enter: "))

    sum_nums = 0

    for i in range(amount):
        next_num = int(input("Enter the next number "))
        sum_nums += next_num

    avg = sum_nums / amount
    print(f"You entered {amount} numbers")
    print(f"The sum of these numbers is {sum_nums}")
    print(f"The average of these numbers is {avg}")

main()