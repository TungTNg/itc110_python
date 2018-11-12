# pizzaCalculator.py
# A program to calculate the cost per square inch of a circular
# by Tung Nguyen

import math

def main():
    # declare program function:
    print("This program calculates the cost per square inch of a pizza.")
    print()
    
    # prompt user to input the pizza diameter in inches:
    diameter = float(input("Enter the diameter of the pizza (in inches): "))
    
    # prompt user to input the price of the pizza in cents:
    price = float(input("Enter the price of the pizza (in cents): "))
    
    # conversion formular (I googled the formular for a circle's area => A=1/4πd^2)
    # then cost per square inch will be price/area:
    area = 1/4 * math.pi * math.pow(diameter, 2)
    cost = price / area
    
    # print out result that was calculated & rounded to the first decimal point:
    print()
    print("The cost is", round(cost, 2), "cents per square inch.")

main()