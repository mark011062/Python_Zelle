import math

def main():
    terms = int(input("How many terms would you like to sum? "))

    sum_series = 0
    sign = 1
    for i in range(1, 2*terms, 2):
        next_term = sign * 4/i
        sum_series += next_term
        sign *= -1

    print(sum_series)
    accuracy = sum_series - math.pi
    print(accuracy)

main()


