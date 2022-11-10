## We want to makesure that  when we call get_admin_password the function is called securely 
# ( it validates if the user access level is valid and then only return the password)
user = {"username": "Mohan", "access_level":"admin"}
user = {"username": "Mohan", "access_level":"user"}

def get_admin_password():
    return "pass123WorD897"

def make_secure(func):
    def secure_fucntion():
        if user["access_level"]=="admin":
            return func()
        else:
            return f"No admin permission for user {user['username']}"
        
    return secure_fucntion

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())


