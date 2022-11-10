# The asterisk takes all the arguments and packs them into a tuple.
# The asterisk can be used to unpack sequences into arguments too!

def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

product = multiply(1, 3, 5)
print(f"Product is {product}")

def add(x, y):
    return x + y

number = [10, 20]
sum_of_num = add(*number)
print(f"sum of numbers {number} is {sum_of_num}")

nums = {"x": 25, "y": 42}
sumofxy = add(**nums)
print(f"sum of numbers {nums} is {sumofxy}")

def apply(*args, operator):
    if operator == "*":
#        return multiply(args)
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "Not a valid operator used"

added_value = apply(1,2,3,4,5, operator= "+")
print(f"Added value is - {added_value}")

multiplied_val = apply(1,2,3,4,5,operator = "*")
print(f"Multiplied value is - {multiplied_val}")