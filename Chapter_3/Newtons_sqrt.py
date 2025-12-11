def main():
    num = float(input("Enter a number to find the square root of: "))
    guess = num/2
    iterations = int(input("How many iterations? "))

    for i in range(iterations):
        guess = (guess + (num / guess)) / 2
        print(f"Iteration {i+1}: {guess}")

    print("\nFinal approximation:", guess)

main()