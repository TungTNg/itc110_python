# futval.py
#    A program to compute the value of an investment
#    carried <user input> years into the future

def main():
    print("This program calculates the future value of a 10-year investment.")
    print()
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate in decimal form (e.g 0.03 for 3%): "))
    year = eval(input("Enter the number of years you want to include in your investment: "))

    for i in range(year):
        principal = principal * (1 + apr)
    
    print ("The value in", year, "years is:", round(principal, 2))

main()
