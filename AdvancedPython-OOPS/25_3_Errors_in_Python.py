def divide(dividend, divisor):
    if(divisor == 0):
        raise ZeroDivisionError("Divisor cannot be zero")
    
        
    return dividend/divisor

grades = []
##grades = [78, 99, 85, 100]

print("Welcome to the Average Calculator Program!!!")

try:
    average = divide(sum(grades),len(grades))
except ZeroDivisionError:
    print("There are no grades yet in your list")
else:
    print(f"The average grade is - {average}")
finally:
    print("Thank you!!!")    