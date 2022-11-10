## importing for itemgetter
from operator import itemgetter
# -- searching with first-class functions --
def search(sequence, search_str, finder):
    for el in sequence:
        if finder(el) == search_str:
            return el
    raise RuntimeError(f"Couldnot find the {search_str} in seqeunce")

friends = [
    {"name": "Abhishek", "age":28},
    {"name": "Sandeep", "age":30},
    {"name": "Gaurav Mishra", "age":27},
    {"name": "Ram", "age":27}
]

def get_friend_name(friend):
    return friend["name"]

print("Starting Search App")
try:
    print(search(friends, "Gaurav Mishra", get_friend_name))
    
    # -- using lambdas since this can be simple enough --
    print(search(friends, "Sandeep", lambda friend: friend["name"]))
    
    ## # -- or as an extra, using built-in functions --
    print(search(friends, "Abhishek", itemgetter("name")))
    
except RuntimeError as r:
    print(r)
finally:
    print("Searching App completed")