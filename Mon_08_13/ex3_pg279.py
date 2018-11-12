def a():
    n = eval(input("enter n: "))
    sum = 0;
    i = 1;
    
    while i <= n:
        sum = sum + i;
        i = i + 1;
        
    print(sum)

a()

def b():
    n = eval(input("enter n: "))
    sum = 0;
    i = 1
    
    while i <= n:
        sum = sum + i;
        i = i + 2;
    
    print(sum)
    
b()

def c():
    sum = 0;
    x = 0;
    
    while x!= 999:
        sum = sum + x
        x = int(input("Enter a number. 999 to exit: "))
        
    print(sum)
    
c()

def d():
    count = 0;
    n = int(input("enter n: "))
    
    while n > 1:
        n = n // 2
        count = count + 1
        
    print(count)

d()