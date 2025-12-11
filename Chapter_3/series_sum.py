def main():
    count_of_nums = int(input("Enter the number of numbers to sum: "))
    current = count_of_nums
    sum = 0
    for i in range(count_of_nums):
        n = int(input("Enter the next n: "))
        sum += n
        current -= count_of_nums

    print(f"The sum of the {count_of_nums} numbers you entered is {sum}")

main()

