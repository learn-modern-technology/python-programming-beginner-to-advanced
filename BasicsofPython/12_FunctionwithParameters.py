# -- function to add x and y
def add1(x, y):         ## x and y are called parameters
    result = x + y
    print(f"result from add1 function - {result}")

add1(2, 3)  # 2 and 3 are called arguments

def add(x, y):
    result = x + y
    return result

result = add(2, 3)
print(f"result from add function - {result}")
# -- If a function doesn't have parameter, you can't give it arguments --

def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Shantanu")

def say_hello(name):
    print(f"Hello, {name}!")

say_hello(name="Neha Kakkar")  # Obvious that this is someone's name


def divide(dividend, divisor):
    if divisor != 0:
        print(f" {dividend} / {divisor} is equal to {dividend / divisor}")
    else:
        print("You fool!")


divide(dividend=15, divisor=3)  ## Recommended use for better readability
divide(15, 0)
divide(15, divisor=0)  # That's OK
# divide(dividend=15, 0)  # Not OK, named arguments must go after positional arguments 
# I recommend you use keyword arguments whenever possible, just because it makes things much more readable and maintainable long-term.

# This coding exercise has two parts:
# Create a function, user_name() , which returns the string "Rolf" .
# Create a function, greeting() , which takes a name as an argument and returns "Hello, NAME, how are you?" 

def user_name():
    name = "Rolf"
    return name

def greeting(name="Manohar"):           ## This is default parameter
    return f"Hello, {name}, how are you?"

user = user_name()
greeting_message = greeting(user)
print(greeting_message)

greeting_message2 = greeting()
print(greeting_message2)


def add(x, y=3):
    print(x + y)


add(5)  # 8
add(5, 8)  # 13
#add(y=3)  # Error, missing x

# -- Order of default parameters --
# def add(x=5, y):  # Not OK, default parameters must go after non-default
#     print(x + y)
# -- Usually don't use variables as default value --

default_y = 3

def add(x, y=default_y):    ## y=3 is used while creating the functions and it can't be changed So we usually don't pass default value to variables in a function
    sum = x + y
    print(sum)

add(2)  # 5
default_y = 4
print(default_y)  # 4
add(2)  # 5, even though we re-defined default_y

## Returning from functions
def add(x, y):
    print(x + y)

add(5, 8)
result = add(5, 8)
print(result)  # None

# If we want to get something back from the function, it must return a value.
# All functions return _something_. By default, it's None.

# -- Returning values --
def add(x, y):
    return x + y

add(1, 2)  # Nothing printed out anymore.
result = add(2, 3)
print(result)  # 5

# -- Returning terminates the function --
def add(x, y):
    return
    print(x + y)
    return x + y

result = add(5, 8)  # Nothing printed out
print(result)  # None, as is the first return

# -- Returning with conditionals --
def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

result = divide(15, 3)
print(result)  # 5

another = divide(15, 0)
print(another)  #You fool!