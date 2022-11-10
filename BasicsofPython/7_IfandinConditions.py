day_of_the_week = input("Which day of the week is it today?")
if (day_of_the_week == "Monday"):
    print(f"Today is {day_of_the_week}. Have a great start of the week")
elif(day_of_the_week == "Friday"):
    print(f"Today is {day_of_the_week}. Have a great weekend !!")
else:
    print(f"Today is {day_of_the_week}. Full Speed ahaead")
    
day_of_the_week2 = input("Which day of the week is it today?").lower()

if (day_of_the_week2 == "monday"):
    print(f"Today is {day_of_the_week2}. Have a great start of the week")
elif(day_of_the_week2 == "friday"):
    print(f"Today is {day_of_the_week2}. Have a great weekend !!")
else:
    print(f"Today is {day_of_the_week2}. Full Speed ahaead")

# To use "in" in Python with List
friends = ["Mohit", "Rohit", "Gaurav", "Shantanu", "Sandeep", "RekhaRam", "Shivam", "Abhishek"]
print("Whether Kapil is in the friendlist ?","Kapil" in friends)
print("Whether Rohit is in the friendlist ?","Rohit" in friends)

## To use "in" in Python with Sets
movies_watched = {"The Matrix", "World War Z", "The Money Heist", "The Criminal Justice", "Shiddat", "Rustom"}
user_movie = input("Enter something you've watched recently: ")
print("User watched one of the listed movies -",user_movie in movies_watched)

### To use "in" in Python with Tupple
tmovies_watched = ("The Matrix", "World War Z", "The Money Heist", "The Criminal Justice", "Shiddat", "Rustom")
tuser_movie = input("Enter something you've watched recently: ")
print("User watched one of the listed movies -",tuser_movie in tmovies_watched)

# The `in` keyword works in most sequences like lists, tuples, and sets.

if user_movie in movies_watched:
    print(f"I have watched {user_movie} too !!")
else:
    print("I haven't watched that movie yet")
# Let's suggest them to play the game
number = 9
user_input = input("Enter y if you want to play the game - Guessing Number").lower

if user_input == "y":
    user_number1 = int(input("Enter the number that you want to guess "))
    if user_number1 == number:
        print("You have guessed it right")
    else:
        print(f"Hard luck. The guessed number {user_number1} is incorrect")
else:
    print("Thank you!! You choose not to play the guessing game")

user_input2 = input("Enter y if you want to play the game - Guessing Number")

if user_input in ("y","Y"):
    user_number2 = int(input("Enter the number that you want to guess "))
    if user_number2 == number:
        print("You have guessed it right")
    elif number - user_number2 in (1, -1):
        print("You were off by 1")
    else:
        print(f"Hard luck. The guessed number {user_number2} is incorrect")
else:
    print("Thank you!! You choose not to play the guessing game")
    
user_input3 = input("Enter y if you want to play the game - Guessing Number")
if user_input.lower() == "y":
    user_number3 = int(input("Enter the number that you want to guess "))
    if user_number3 == number:
        print("You have guessed it right")
    elif abs(number - user_number3) == 1:
        print("You were off by 1")
    else:
        print(f"Hard luck. The guessed number {user_number3} is incorrect")
else:
    print("Thank you!! You choose not to play the guessing game")