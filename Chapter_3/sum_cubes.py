def main():
     n = int(input("Enter n: "))
     sum = 0
     current = n

     for i in range(n):
         sum += current**3
         current -= 1

     print(f"The sum of the cubes of the first {n} numbers is {sum}")

main()