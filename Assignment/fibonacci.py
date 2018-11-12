def main():
    # declare the program function
    print("This program calculates the nth Fibonacci value.")
    print()

    # declare 3 main variable we'll use (fn-1, fn, fn+1 //fibo) & the counter i
    fn = 1
    fn_1 = 0
    i = 1
    fibo = 0
    
    # promp user input
    n = int(input("Enter the value of n: "))
    
    # main logic, after every loop, fn+1 /fibo number will be created as the sum of fn + f(n-1)
    # then the current number fn become fibbo (to be waiting for next loop) & fn-1 = fn (last fn)
    while (i < n):
        fibo = fn + fn_1
        fn_1 = fn
        fn = fibo
        i = i + 1

    #print out result
    print("The " + str(n) + "th Fibonacci number is " + str(fibo))
    
main()