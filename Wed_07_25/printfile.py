# printfile.py
# print a file content to the screen

def main():
    infile = open("names.txt", "r")
    data = infile.read()
    print(data)
    
main()