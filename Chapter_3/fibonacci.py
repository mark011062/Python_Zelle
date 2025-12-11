
def main():
    terms = int(input("Which term would you like to see the sum of? "))

    current = 1
    previous = 1
    for i in range(2,terms):
        next_value = previous + current
        previous = current
        current = next_value

    print(current)

main()