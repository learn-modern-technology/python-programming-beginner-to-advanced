def isarmstrong(num):
    astr = str(num)
    num2 = num
    nodigit = len(astr)
    print(f"No of digits in {num} is {nodigit}")
    if nodigit > 0:
        sum = 0
        while num != 0:
            sum = sum + pow((num%10), nodigit)
            num = int(num/10)
        if num2 == sum:
            return True
        else:
            return False

def narmstrong(start_limit, end_limit):
    for x in range(start_limit, end_limit+1):
        ## print (f"x is {x}")
        num1 = x
        num =  x
        sum = 0
        no_of_digit = len(str(x))
        ## print (f"no_of_digit is {no_of_digit}")
        while(num > 0):
            rem = num % 10
            sum = sum + (rem ** no_of_digit)
            num = int(num/10)

        if (num1 == sum):
            print(f"{num1} - is a armstrong number")

if __name__ == "__main__":
    number_to_test = 153
    validate = isarmstrong(number_to_test)
    if validate:
        print(f"{number_to_test} is a armstrong number")
    else:
        print(f"{number_to_test} is not a armstrong number")
        
    narmstrong(1, 10000)