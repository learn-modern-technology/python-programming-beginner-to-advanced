# -- Unpacking kwargs --
def named(**kwargs):
    print(kwargs)

named(name="Mohan", age =35)

details = { "name":"Rajamohan", "age": 38}

named(**details)

# -- Unpacking and repacking --
def named(**kwargs):                    #converts arguments into dictionary
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)                     # Unpack the dictionary into keyword arguments.
    for name, age in kwargs.items():    # kwargs is a dictionary that can be accessed by using items()
        print(f"{name} : {age}")

print_nicely(name="Priyanka", age=30)

details = { "name":"Rajshekar", "age": 38}
print_nicely(**details)

# -- Both args and kwargs --
# This is normally used to accept an unlimited number of arguments and keyword arguments, such that some of them can be passed onto other functions.
# You'll frequently see things like these in Python code:
"""
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""
# While the implementation is irrelevant at this stage, what it allows is for the caller of `post()` to pass arguments to `request()`.
def both(*args, **kwargs):
    print(f"args - {args}")
    print(f"kwargs - {kwargs}")

both(1,2,3,4,5,6,7,8, name="Chandini", age=28)

# -- Error when unpacking --
def myfunction(**kwargs):
    print(kwargs)

#myfunction(**"Bob")  # Error, must be mapping
#myfunction(**None)  # Error

## We will see how to program below objects using OOPS
student = {"name": "Rajaram", "grades": (88, 73, 92, 96, 97)}

def average(sequence):
    return f"Average is - {sum(sequence)/ len(sequence)}"

print(average(student["grades"]))