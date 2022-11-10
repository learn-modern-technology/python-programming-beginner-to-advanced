user = {"username": "Sudhanshu", "access_level":"user"}

def get_admin_password():
    return "pass123WorD897"

## print(get_admin_password()) ## Prints the admin password even for "guest" user

if user["access_level"]=="admin":       ## IT gives some protection but we can still print the password outside the condition as in line 11
    print(get_admin_password())

## print(get_admin_password())     # The function itself is still unsecured

## Writing secure function----------
def secure_get_admin():
    if user["access_level"]=="admin":
        print(get_admin_password())

# Now secure_get_admin() is secure.
# But get_admin_password() is still around, and I could call it:

secure_get_admin()
print(get_admin_password())

# We want to get rid of get_admin_password so that only the secure function remains!
# Maybe something like this
def secure_function(func):
    if user["access_level"] == "admin":
        return func
    
user = {"username": "Mohan", "access_level":"admin"}

get_admin_password = secure_function(get_admin_password)
print(get_admin_password())


# When we ran `secure_function`, we checked the user's access level. Because at that point the user was not an admin, the function did not `return func`.
# Therefore `get_admin_password` is set to `None`.

# We want to delay overwriting until we run the function
## We want to makesure that  when we call get_admin_password the function is called securely 
# ( it validates if the user access level is valid and then only return the password)     