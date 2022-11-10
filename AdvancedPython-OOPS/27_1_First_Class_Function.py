# A first class function just means that functions can be passed as arguments to functions.

def calculate(*values, operator):
    return operator(*values)

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can't be 0")
    
    return dividend/ divisor

def average(*values):
    return sum(values)/len(values)

print("Welcome to the Division demo using First Class Function")
try:
    result = calculate(20,5, operator=divide)
    print(result)
except ZeroDivisionError as z:
    print(z)
finally:
    print("Division App completed its task or process")


print("Welcome to the Average calculation using First Class Function")
try:
    result = calculate(20, 30, 35, 45, 55, 65, 70, operator=average)
    print(result)
except ZeroDivisionError as z:
    print(z)
finally:
    print("Average App completed its task or process")
