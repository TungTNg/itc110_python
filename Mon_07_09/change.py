# change.py
# A program to calculate the value of some change in dollars

def main():
    print('This program will convert value of some changes to dollar value')
    print()
    quarter = int(input('Please enter the amount of quaters: '))
    dime = int(input('Please enter the amount of dimes: '))
    nickel = int(input('Please enter the amount of nickel: '))
    cent = int(input('Please enter the amount of cent: '))
    dollar = 0.25*quarter + 0.1*dime + 0.05*nickel + 0.01*cent
    print()
    print('The total amount of dollar value is: $' + str(round(dollar, 2)))
main()