from libs import mylib

print("In mymodule.py -", __name__,"\n")

def divide(dividend:int, divisor:int):
    return f"Answer is {dividend/divisor}"