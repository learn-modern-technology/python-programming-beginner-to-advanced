import functools

user = {"username": "Mohan", "access_level":"admin"}
#user = {"username": "Mohan", "access_level":"user"}

def make_secure(func):
    @functools.wraps(func)
    def secure_fucntion(panel):
        if user["access_level"]=="admin":
            return func(panel)
        else:
            return f"No admin permission for user {user['username']}"
        
    return secure_fucntion


@make_secure
def get_password(panel):
    if panel == "admin":
        return "pass123WorD897"
    elif panel == "billing":
        return "super_secure_password"
## Since we have parameterized the function - get_password(), we have to modify secure_fucntion() and func() 
## line 8 and 10 as well. Until we don't modify this, when we call the function with arguments, it will not work.
## This is not good practice. We can use *args and **kwargs in the line 8 and 10
## We can also use this secure_fucntion with any other fucntions.
## The only condition is when we are calling the function get_password the correct argument 
## must be passed to get valid output
print(get_password("admin"))
print(get_password)
print(get_password.__name__)  


import functools
user = {"username": "Mohan", "access_level":"admin"}
#user = {"username": "Mohan", "access_level":"user"}

def make_secure(func):
    @functools.wraps(func)
    def secure_fucntion(*args, **kwargs):
        if user["access_level"]=="admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permission for user {user['username']}"
        
    return secure_fucntion


@make_secure
def get_password(panel):
    if panel == "admin":
        return "pass123WorD897"
    elif panel == "billing":
        return "super_secure_password"
## Since we have parameterized the function - get_password(), we have to modify secure_fucntion() and func() 
## line 8 and 10 as well. Until we don't modify this, when we call the function with arguments, it will not work.
## This is not good practice. We can use *args and **kwargs in the line 8 and 10
## We can also use this secure_fucntion with any other fucntions.
## The only condition is when we are calling the function get_password the correct argument 
## must be passed to get valid output
print(get_password("billing"))
print(get_password)
print(get_password.__name__)