def validPrime(num):
    num2 = num
    divisible_flag = False
    x = 0
    for x in range(2, num+1):
        if (num % x == 0):
            divisible_flag = True
            break
        else:
            continue
        
    if ((num2 == x) and (divisible_flag)):
        return True
    else:
        return False
    
def listnPrime(lower_limit, upper_limit):
    list_prime = []
    for num2 in range(lower_limit, upper_limit+1):
        num  = num2
        divisible_flag = False
        x = 2
        if (num == 0 or num == 1):
            continue
        else:
            for x in range(2, num+1):
                if (num % x == 0):
                    divisible_flag = True
                    break
                else:
                    continue
                    
            if ((num2 == x) and (divisible_flag)):
                list_prime.append(num2)

    return list_prime

def PrintnPrime(lower_limit, upper_limit):
    for num2 in range(lower_limit, upper_limit+1):
        ## num2 = number
        if (validPrime(num2)):
            print(f"Number {num2} - is a Prime Number")
        else:
            print(f"Number {num2} - is not a Prime Number")


if __name__ == "__main__":
    number = 243
    from_num = 1
    to_num = 1000
    print(f"{number} is a Prime ? - {validPrime(number)}")
    print(f"List of Prime numbers from {from_num} to {to_num} is")
    print(listnPrime(from_num, to_num))
    PrintnPrime(1, 100)
    
    