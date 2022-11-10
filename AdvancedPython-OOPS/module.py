def divide(dividend:int, divisor:int):
    return dividend / divisor

## We will use __name__ to identify in which file we are in.
## This will help us to differentiate which file we are in and from which file we are importing

print("In module.py - ", __name__)

## This is the output when we run this module.py
## In module.py -  __main__
## The reason we got __main__ as output is beacuse at the time of execution
## python would have updated __name__ = __main__

import libs.mylib
print("In module.py:", __name__)