# sumExercise.py
# a program to print out sum of user inputs

def main():
    userName = input('What\'s your name? ' )
    print('Hello,', userName ,'welcome, to sum calculator')
    print()
    firstNum = eval(input('Enter first number: '))
    secondNum = eval(input('Enter second number: '))
    print('The sum of' , firstNum , '+' , secondNum , '=' , firstNum + secondNum)
    
main();