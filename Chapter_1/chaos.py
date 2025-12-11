#File: chaos.py
#A simple program illustrating chaotic behavior

def main():
    print("This program illustrates a chaotic function")
    nums = int(input("Enter the number values to return: "))
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(nums):
        x = 3.9 * x * (1-x)
        print(x)

main()
