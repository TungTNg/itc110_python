# wordCalculator.py
# A program to calculate the number of words in a sentence
# by Tung Nguyen


def main():
    # declare program function:
    print("This program calculates the number of words in a sentence.")
    print()
    
    # prompt user to input the sentence:
    sentence = input("Enter a phrase: ")
    
    # split the sentence into a list that contains words
    listWord = sentence.split()
    
    # count the number of words inside the list
    countWord = len(listWord)
    
    # print out the number of words as the result
    print()
    print("Number of words:", countWord)

main()