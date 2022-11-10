import os
from pickle import FALSE, NONE
from statistics import mean
from audioop import reverse
import sys
os.path.dirname(sys.executable)

print(os.path.dirname(sys.executable))
print(sys.executable)

marks1 = [10,20,30,40,50,60,70,80,90,100]
marks2 = [1,2,3,4,5,6,7,8,9,11]
marks3 = [15,25,35,45,55,65,75,85,95,105]
print('marks1 -',marks1)
print('marks2 -',marks2)
print('marks3 -',marks3)

## marks1+=marks2
## print('Marks1 + Marks2 -', marks1)

marks1[1:3]+=marks2
print('marks1 =Marks1 + Marks2 -', marks1)

marks4 = marks3[1:3]+marks2
print('marks4 = Marks3 + Marks2 -', marks4)

marks5 = marks3[1:]+marks2
print('marks5 = Marks3 + Marks2 -', marks5)

marks5.sort(reverse=False)
print('Sorting of marks5',marks5 )

marks5.sort(reverse=True)
print('Sorting of marks5',marks5)

marks3.insert(10,135)
print('Marks 3-',marks3)

marks3.insert(11,125)
print('Marks 3-',marks3)

print('Index of values 135 in marks3 list is -',marks3.index(135,0))

marks5.append(marks3)
print('Marks5 after appending with Marks3 is ',marks5)

marks2.append(marks3[:])
print('Marks2 after appending with Marks3 is ',marks2)

marks2.append(marks3[5])
print('Marks2 after appending with Marks3 is ',marks2)

marks6 = marks3.copy()
print('Marks6 after running copy of marks Marks3 is ',marks3)

Total = sum(marks6)
print('Total in the list Marks6 is ',Total)
print('Average of marks6 is',mean(marks6))


team1=['Dennis Ritchie', 'Alfred Aho', 'Edsger Dijkstra', 'James Gosling', 'Charles Babbage', 'Jacob Millman', 'Donald Knuth', 'Ken Thompson', 'Brian Kernigham', 'Jeffrey Ullman']
##print(team1.index('Jacob',0))   ##ValueError: 'Jacob' is not in list
print('Position of Jacob Millman in the list is -',team1.index('Jacob Millman',0))
print('Team 1 List is -', team1)
team2=team1.copy()
print('Team 2 List is -', team2)

team2.reverse()
print('Team 2 List in reverse order -', team2)
team2.sort(reverse=False)
print('Team 2 List in Ascending order -', team2)
team2.sort(reverse=True)
print('Team 2 List in Descending order -', team2)

print('Length of list team2 -', len(team2))
print('Index of Last Element of list is team2 ',team2.index('Alfred Aho',len(team2)-1))
print('Last Element of list team2 ',team2[len(team2)-1])

##team2[10] = 'Turaam Singh' ##IndexError: list assignment index out of range
print('Team 2 List-', team2)

team2.append('Turam Singha')
print('Last Element of list team2 after append ',team2[len(team2)-1])

team2.insert(len(team2)-1,"Alexa from Amazon")
print('Last Element of list team2 after append ',team2[len(team2)-3:len(team2)])
print('Min Element of list team2 after append ',min(team2))
print('Max Element of list team2 after append ',max(team2))

numbers = [1, 3, 5]
squares = [x * 2 for x in numbers]

# -- Dealing with strings --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)


# -- Can make a new list of friends whose name starts with S --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)

# -- List comprehension creates a _new_ list --

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]  # same as above

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends), " starts_s: ", id(starts_s))
