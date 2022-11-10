## We want to makesure that  when we call get_admin_password the function is called securely 
# ( it validates if the user access level is valid and then only return the password)
import functools


user = {"username": "Mohan", "access_level":"admin"}
#user = {"username": "Mohan", "access_level":"user"}

def make_secure(func):
    @functools.wraps(func)
    def secure_fucntion():
        if user["access_level"]=="admin":
            return func()
        else:
            return f"No admin permission for user {user['username']}"
        
    return secure_fucntion

## get_admin_password = make_secure(get_admin_password)
## we can rewrite above fuction in simple way by just editing "@make_secure at the top of the function"

@make_secure
def get_admin_password():
    return "pass123WorD897"

print(get_admin_password())
print(get_admin_password)
print(get_admin_password.__name__)     


## The problem with @make_secure and other way to make this fucntion as secure is that 
## these functions are not registed with python internally. instead it is registered as secure_function
## <function make_secure.<locals>.secure_fucntion at 0x000002901C12F130>
## <function make_secure.<locals>.secure_fucntion at 0x000002901C12F130>
## secure_fucntion
## so any attachment to the original get_admin_password will be lost.
## we have to attach a decorator named - @functools_wraps to fix this
## this keeps the name and documentation of the function as is, if there are any
## <function get_admin_password at 0x00000233A1550B80>
## get_admin_password

