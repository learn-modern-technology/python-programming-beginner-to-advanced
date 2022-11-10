## Here we will import from module.py file
## we will see various way to import 
from module import divide  ## This way we can import a specific function from module.py
print(divide(10,3))
print(__name__)

## or otherwise we can simply import the entire file as is using below syntax
import module
## we will access the divide() from module using module.divide
print(module.divide(13,2))

import sys
print(sys.path) 
## This prints the path and these are defined in specific order
## The 1st set will be always File path (where our code is saved and from where we are executing the code)
## The 2nd will be always python path. 
## And then we will have remaining set of paths

# -- circular imports --
# Make mymodule.py import code.py as well.

# -- importing from a folder -
import module

print("\n\n In 23_2_how_to_use_import.py -",__name__, "\n\n")

import sys
print(sys.modules)