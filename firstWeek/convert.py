#convert.py
# A program to convert Celsius temps to Fahrenheit

def main():
    for celsius in range(0, 101, 10):
        fahrenheit = (9/5) * celsius + 32
        print("The temperature is ",fahrenheit," degrees Fahrenheit at", celsius, "celsius degrees.")

main()
