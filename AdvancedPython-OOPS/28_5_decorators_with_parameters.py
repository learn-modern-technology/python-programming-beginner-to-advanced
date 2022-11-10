import functools
user = {"username": "Mohan", "access_level":"user"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_fucntion(*args, **kwargs):
            if user["access_level"]==access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permission for user {user['username']}"
            
        return secure_fucntion
    return decorator


@make_secure("admin")
def get_admin_password():
    return "admin: admin1234"

@make_secure("user")
def get_dashboard_password():
    return "user: pass123WorD897"

print(get_admin_password())
## print(get_admin_password)
## print(get_admin_password.__name__)
## 
print(get_dashboard_password())
## print(get_dashboard_password)
## print(get_dashboard_password.__name__)

user = {"username": "Sathya", "access_level":"admin"}

print(get_admin_password())
## print(get_admin_password)
## print(get_admin_password.__name__)
## 
print(get_dashboard_password())
## print(get_dashboard_password)
## print(get_dashboard_password.__name__)
