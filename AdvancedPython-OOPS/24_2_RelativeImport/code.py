## This is a relative import example
##from .mymodule import divide  ## This import will error 
## ImportError: attempted relative import with no known parent package
## It doesn't allow to import from the current directory using ".mymodule"
## We can try this from subfolders Please see the example in mymodule.py file
from mymodule import divide

print("In code.py - ",__name__,"\n")

print(divide(267,15))