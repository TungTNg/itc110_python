# factorial.py
# Program to compute the factorial of a number
# Illustrates for loop with an accumulator


def main():
    n = int(input('Enter a whole number: '))
    fact = 1
    for factor in list(range(1, n+1, 1)):
        fact = factor * fact
    print('The factorial of' , n, 'is', fact)
    
    print(list(range(1, n+1))) #just to see the list they go through
    
main()
