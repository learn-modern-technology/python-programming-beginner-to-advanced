## To calculate Compound Interest
def calculate_ci(p,r,t):
    if (p == 0 or r == 0 or t == 0):
        return 0
    else:
        a = p*(pow((1 + (r/100)),(t/12)))
        return a

principal = 10000
rate = 10
time_in_months = 36
amount = calculate_ci(principal, rate, time_in_months)
interest = amount - principal
if interest == 0:
    print(f"Principal is - Rs.{principal}, \nRate of Interest p.a is - {rate}%, \nTime duration in months is - {time_in_months} months")
    print(f"Interest can't be calculated as one of the Principal, Rate or Time duration is ZERO")
else:
    print(f"Principal is - Rs.{principal}, \nRate of Interest p.a is - {rate}%, \nTime duration in months is - {time_in_months} months")
    print(f"Calculated Interest is - Rs.{interest}")
    print(f"Total Amount including Interest is - Rs.{amount}")