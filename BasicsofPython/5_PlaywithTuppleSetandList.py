l = ["Molly","Ashok","Bipin"]  ## This is a list. We can add or remove element in Tupple
t = ("Molly","Ashok","Bipin")   ## This is a Tupple. We can't add or remove element in Tupple
s = {"Molly", "Ashok", "Bipin"}  ## This is a Set. We can't have duplicate element in Set. The Order of element in the Set is not guaranteed
print(l)
print(t)
print(s)

print(f"Type of variable l is {type(l)}")
print(f"Type of variable t is {type(t)}")
print(f"Type of variable s is {type(s)}")

print(l[0])
print(t[0])
# print(s[0])  # TypeError: 'set' object is not subscriptable This gives an error because sets are unordered, so accessing element 0 of something without order doesn't make sense.
l[0] = "Rajkumar"
# t[0] ="Mahesh"  # TypeError: 'tuple' object does not support item assignment
print(l)
print(t)
print(s)

# Add to a list by using `.append`
l.append("Helen")
print(l)
# Tuples cannot be appended to because they are immutable.

# Add to sets by using `.add`
s.add("Suresh")
print(s)

# Sets can't have the same element twice.

s.add("Suresh")
print(s)

s.remove("Suresh")
print(s)