## Type hinting is available in python 3.5 and above
### Hinting will help us identify the errors before running the python interpretor 
from typing import List  ## can also import Tupple, Set

def list_avg(sequences:List) -> float:
    return (sum(sequences)/len(sequences))

##list_avg(1234)

list_seq = [10,20,30,40,50,60,70,80,90]
avg = list_avg(list_seq)
print(avg)

### avg2 = list_avg(1,2,3,4,5,6,7,8,9,10)   ##TypeError: list_avg() takes 1 positional argument but 10 were given
avg2 = list_avg([1,2,3,4,5,6,7,8,9,10])
print(avg2)