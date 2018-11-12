# numbers2text.py
# convert a sequence of Unicode numbers to a string of text

def main():
    print("Convert a sequence of Unicode numbers to a string of text")
    
    #get the message to encode
    inString = input("Enter the Unicode encoded message: ")
    
    message = ""
    
    print(inString.split())
    
    for numStr in inString.split():
        codeNum = chr(int(numStr) - 3)
        message = message + codeNum
        
    print("The decoded message is: ", message)
    
main()
        