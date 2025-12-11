
def main():
    n = int(input("Enter a value for n "))
    sum = 0
    current = n
    for i in range(n):
        sum += current
        current -= 1

    print(f"The sum of the first {n} numbers is {sum}")

main()