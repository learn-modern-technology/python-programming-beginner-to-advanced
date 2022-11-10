users = [
    (0, "Maheshwar", "password"),
    (1, "Aruneshwar", "bob123"),
    (2, "Shiva", "longp4assword"),
    (3, "Vishnu", "1234"),
]

userid_mapping = {user[0]: user for user in users}
print(f"userid_mapping - {userid_mapping}")
username_mapping = {user[1]: user for user in users}
## username_mapping = {user[1] for user in users}
print(f"username_mapping - {username_mapping}")
print(username_mapping["Vishnu"])

# -- Can be useful to log in for example --
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect.")

# If we didn't use the mapping, the code would require us to loop over all users.
# Shown on the side, pause the video if you want to read it thoroughly.