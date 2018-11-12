# convert month given as a number to the month abbreviation

def main():
    #create a list for the months 
    months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "Octorber", "November", "December"]
    
    n = int(input("Enter a month number between 1 and 12: "))
    
    print("The month is", months[n-1] + ".")
    
main()