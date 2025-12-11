#A program to convert Celcius to Farenheit

def main():
    print("Hey there! I'm here to convert the temp from Celcius to Farenheit for you!!!")
    for temperature in range(0, 110, 10):
        celcius = temperature
        farenheit = (9/5) * celcius + 32
        print(f"The temperature in Farenheit is {farenheit} degrees")

main()

input("Press the <ENTER> key to quit.")