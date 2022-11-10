def hello():
    print("Hello World!!")
    
hello()


def user_age_in_seconds():
    age_in_years= int(input("Please enter your age"))
    age_in_seconds= age_in_years * 365 *24 *60 *60
    print(f"Your age in seconds is {age_in_seconds}")


print("Welcome to the age in seconds program!")
user_age_in_seconds()

print("Good Bye!!")

# print("Welcome to the friends Group")
# friends = ["RekhaRam", "Shantanu", "Gaurav"]
# 
# def add_friend():
#     friend_name = input("Enter your friend name: ")
#     # Another wrong way of adding to a list! 
#     #friends = friends + [friend_name]  ## UnboundLocalError: local variable 'friends' referenced before assignment
#     f = friends + [friend_name]
#     print(f"friends - {f}")
#     return f
# 
# friends = add_friend()
# print(f"friends- {friends}")

## Scenario 2
# def add_friend():
#     friends.append("Mahesh")
# 
# friends = []
# add_friend()
# 
# print(f"friends - {friends}")

## Scenario 3
# def add_friend():
#     friend_name = input("Enter your friend name: ")
#     friends.append(friend_name)
# 
# 
# friends = []
# add_friend()
# print(f"friends - {friends}")

# Scenario 4
friends = []
def add_friend():
    friend_name = input("Enter your friend name: ")
    friends.append(friend_name)


add_friend()
add_friend()
add_friend()
add_friend()
add_friend()

print(f"friends - {friends}")