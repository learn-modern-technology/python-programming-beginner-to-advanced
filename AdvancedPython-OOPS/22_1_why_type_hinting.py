## Type hinting is available in python 3.5 and above
### Hinting will help us identify the errors before running the python interpretor 
from typing import List
def list_avg(sequences):
    return(sum(sequences)/len (sequences))

list_seq = [10,20,30,40,50,60,70,80,90]
avg = list_avg(list_seq)
print(avg)

avg2 = list_avg(1,2,3,4,5,6,7,8,9,10)
print(avg2)