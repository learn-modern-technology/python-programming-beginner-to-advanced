from collections import deque
from queue import Queue
from queue import LifoQueue
import os
import sys
os.path.dirname(sys.executable)

print(os.path.dirname(sys.executable))
print(sys.executable)

# Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner. 
# With a queue the least recently added item is removed first. 
# A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.

queue_list = (['India','Australia', 'England', 'West Indies', 'New Zeland', 'South Africa', 'Sri Lanka'])
print('Initial Queue')
print(queue_list)

# Removing element from queue
print(queue_list.pop(4))
print('Queue after removing element from list')
print(queue_list)

#Adding element to queue using append and insert
print(queue_list.append("Pakistan"))
print('Queue after adding 1st element from list')
print(queue_list)
queue_list.insert(0,"Bangladesh")
queue_list.insert(6,"Malasiya")
print('Queue after adding 2nd element from list')
print(queue_list)

# Using pop to remove the last element
print(queue_list.pop())
print(queue_list.pop())
print(queue_list.pop())
print(queue_list.pop())
print('Queue after removing element from list')
print(queue_list)


## ### #### ###### ###### ###### ##### ##### ###### ### ####### #### #### ##### #### ##### #### ###### ## ## ## ## ##
# Python program to
# demonstrate stack implementation
# using list

stack = []

# append() function to push
# element in the stack
stack.append("India")
stack.append("England")
stack.append("Australia")

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('Elements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# Python stack can be implemented using the deque class from the collections module.
# Deque is preferred over the list in the cases where we need quicker append and 
# pop operations from both the ends of the container

# Python program to demonstrate stack implementation using collections.deque

from collections import deque

stack = deque()

# append() function to push
# element in the stack
stack.append('India')
stack.append('Australia')
stack.append('Japan')
stack.append('HongKong')

print('Initial stack:')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

## #######  ##  ##  ######  ####### ########    ###################
# Program to demonstrate stack implementation using queue module

# Initializing a stack
stack = LifoQueue(maxsize=5)

# qsize() show the number of elements in the stack
print(stack.qsize())

# put() function to push element in the stack
stack.put('India')
stack.put('Australia')
stack.put('England')
stack.put('West Indies')
stack.put('SriLanka')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())

#######  ####   ################    ##################3

# Python code to demonstrate Queue using deque
queue1 = deque(["Ram", "Tarun", "Asif", "John"])
print(queue1)
queue1.append("Akbar")
print(queue1)
queue1.append("Birbal")
print(queue1)
print(queue1.popleft())				
print(queue1.popleft())				
print(queue1)
