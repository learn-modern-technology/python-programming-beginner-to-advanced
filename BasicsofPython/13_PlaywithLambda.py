# Lambdas are meant to be short functions, often used without giving them a name.
# For example, in conjunction with built-in function map
# map applies the function to all values in the sequence
# -- Important to remember --
# Lambdas are just functions without a name.
# They are used to return a value calculated from its parameters.
# Almost always single-line, so don't do anything complicated in them.
# Very often better to just define a function and give it a proper name

def add(x, y):
    return x + y

print(add(5, 7))

# -- Written as a lambda --
add = lambda x, y: x + y
print(add(5, 7))

## Not recommended to use in this way
print((lambda x, y : x + y)(15 ,17))

def double(x):
    return x * 2

sequences = [1,2,3,4,5,6]
print(f"sequences are {sequences}")
doubled = [double(x) for x in sequences]
print(f"doubled is {doubled}")

## Write using Lambda
sequences3 = [1,2,3,4,5,6]
print(f"sequences3 are {sequences3}")
doubled3 = [(lambda x : x * 2)(x) for x in sequences3]
print(f"doubled3 is {doubled3}")

sequences2 = [1,2,3,4,5,6]
print(f"sequences2 are {sequences2}")
doubled2 = map(double,sequences2)
print(f"doubled2 is {list(doubled2)}")
