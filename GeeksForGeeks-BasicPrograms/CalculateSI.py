## To Calculate Simple Interest
def calculate_si(p,r,t):
    if (p == 0 or r == 0 or t == 0):
        return 0
    else:
        return (p * r * (t/12))/100

if __name__ == "__main__":
    principal = 10000
    rate = 10
    time_in_months = 12
    interest = calculate_si(principal, rate, time_in_months)
    amount = principal + interest
    if interest == 0:
        print(f"Principal is - Rs.{principal}, \nRate of Interest p.a is - {rate}%, \nTime duration in months is - {time_in_months} months")
        print(f"Interest can't be calculated as one of the Principal, Rate or Time duration is ZERO")
        print(f"Total Amount is same as Principal - Rs.{amount}")
    else:
        print(f"Principal is - Rs.{principal}, \nRate of Interest p.a is - {rate}%, \nTime duration in months is - {time_in_months} months")
        print(f"Calculated Interest is - Rs.{interest}")
        print(f"Total Amount including Interest is - Rs.{amount}")
