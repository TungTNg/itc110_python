# mpg.py

def main():
    
    anotherTrip = "y"
    while anotherTrip == "y":
        gallon = float(input('Please enter the amount of gallon you\'ve used so far: '))
        mile = float(input('Please enter the amount of mile you\'ve travel so far: '))
        
        if mile > 0 and gallon > 0:
            mpg = round(mile/gallon, 2)
            print('Your car\'s mpg is: ' + str(mpg))
        else:
            print("Both entries must be greater than zero. Try again!")
            
        anotherTrip = input('Get entries to another trip? (y/n): ')
        
    print('Goodbye!')
    
main()