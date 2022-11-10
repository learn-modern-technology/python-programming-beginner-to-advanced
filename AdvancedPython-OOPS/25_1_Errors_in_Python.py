def divide(dividend, divisor):
    if(divisor == 0):
        print(f"Divisor can't be Zero. Currently Divisor is - {divisor}")
        return
    
    return dividend/divisor

##print(divide(15,0))

##grades = [78, 99, 85, 100]
grades = [] ## Will display unwanted output rather than Average
print("Welcome to the Average Calculator Program!!!")

## We can handle the below logic using errors in python as well.
if len(grades) == 0:
    print("There is no grades available now")
else:
    average = divide(sum(grades),len(grades))
    print(f"The average grade is - {average}")
