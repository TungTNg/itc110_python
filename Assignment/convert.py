# convert.py
# A program to convert distances measured in Kilometers to Miles
# by Tung Nguyen

def main():
    # declare program function:
    print("This program convert distances measured in Kilometers to Miles.")
    print()
    
    # prompt user to input distance in km:
    kilometer = eval(input("What is the distance in Kilometers? (Enter a number) "))
    
    # conversion formular:
    mile = kilometer * 0.62
    
    # print out result that was converted to mile:
    print("The distance in Miles is:",mile,"miles.")

main()