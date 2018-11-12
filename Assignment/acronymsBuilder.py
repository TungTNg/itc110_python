# acronymsBuilder.py
# A program to build acronyms from a phrase
# by Tung Nguyen


def main():
    # declare program function:
    print("This program builds acronyms.")
    print()
    
    # prompt user to input the sentence:
    sentence = input("Enter a phrase: ")
    
    # split the sentence into a list that contains words
    listWord = sentence.split()
    
    # assign a variable that will be used to store each of the first letter of every word in the sentence
    acronym = ""
    
    # loop through the list of words in the sentence (listWord) -> pick the first letter of every word -> store it in acronym variable
    for x in listWord:
        acronym += x[0].upper()
    
    # print out the result    
    print("The acronym is " + acronym)

main()