from math import sqrt


## To check if a given number is Fibonacci number
## https://www.geeksforgeeks.org/python-program-for-how-to-check-if-a-given-number-is-fibonacci-number/
## A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square
def isPerfectSquare(x):
    sqroot = int(sqrt(x))
    return sqroot**2 == x

def check_fibonacci(n):
    if(isPerfectSquare((5*(n**2)) + 4) or isPerfectSquare((5*(n**2)) - 4)):
        return True
    else:
        return False

def fab_formula(num):
    ## Using the formula for finding the n-th Fibonacci number
    numer = ((1+sqrt(5))**num)-((1-sqrt(5))**num)
    denom = (2**num*sqrt(5))
    val = int(numer//denom)
    return val
    
def fab_series(num):
    fib_series = []
    f1 = 0
    f2 = 1
    fib_series.append(f1)
    fib_series.append(f2)
    if (num > 2):
        for i in range(2, num+1):
            temp = f2 + f1
            f1 = f2
            f2 = temp
            fib_series.append(f2)
    return fib_series

if __name__ == "__main__":
    limit = 12
    fib_list = fab_series(limit)
    print(f"{limit}th element in the series is {fib_list[limit]}")
    print(f"List of Fibonacci series is - {fib_list}")
    print(f"{limit}th element of the series is {fab_formula(limit)}")
    
    k = 89    
    if (check_fibonacci(k) == True):
        print(f"{k} is a Fibonacci Number")
    else:
        print(f"{k} is not a Fibonacci Number")