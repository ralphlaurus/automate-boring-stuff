# Boolean Values: True and False
spam = True
print(spam)

# Comparison Operators: ==, !=, <, >, <=, >=
print(42 == 42) # True
print(42 == 99) # False
print(2 != 3) # True
print(2 != 2) # False

# The == and != operators can actually work with values of any data type.
print('hello' == 'hello') # True
print('hello' == 'Hello') # False
print('dog' != 'cat') # True
print(True != True) # False
print(42 == 42.0) # True
print(42 == '42') # False

# The <, >, <=, and >= operators, on the other hand, work properly only with integer and floating-point values.
print(42 < 100) # True
print(42 > 100) # False
print(42 < 42) # False
eggCount = 42
print(eggCount <= 42) # True
myAge = 29
print(myAge >= 10) # True

# The Difference Between == and = Operators
spam = 42 # assignment statement: put the value on the right into the variable on the left
print(spam)
print(spam == 42) # comparison operator: ask whether the value on the left is equal to the value on the right
print(spam == 99) # False
print(spam) # spam is still 42

# Binary Boolean Operators: and
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

# Binary Boolean Operator: or
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

# Unary Boolean Operator: not
print(not True) # False
print(not not not not True) # True
print(not False) # True

# Mixing Boolean and Comparison Operators
print((4 < 5) and (5 < 6)) # True
print((4 < 5) and (9 < 6)) # False
print((1 == 2) or (2 == 2)) # True

print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2) # Multiple boolean operators

# Flow Control Statements: if statements
name = 'Bob'
if name == 'Alice': # condition or expression
    print('Hi, Alice') # block of code to run if the condition is true

# else statements
if name == 'Alice':
    print('Hi, Alice')
else:
    print('Hello, stranger.')

# elif statements
age = 21
if name == 'Alice':
   print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')

# while loop statements
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

# break statements: yourName.py
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break # exit the loop

print('Thank you!')

# continue statements: swordfish.py
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break

print('Access granted')

# Truthy and Falsely Values: 0, 0.0, '' considered falsely values
name = ''
while not name: # while name == ''
    print('Enter your name:')
    name = input()

print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests: # if numOfGuests != 0
    print('Be sure to have enough room for all your guests.')

print('Done')

# for loop and the range() function
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

total = 0
for num in range(101):
    total = total + num

print(total)

# An equivalent while loop
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1

# The Starting, Stopping, and Stepping Arguments to range()
for i in range(12, 16):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(5, -1, -1):
    print(i)

# Importing Modules
import random, sys, os, math

# printRandom.py
for i in range(5):
    print(random.randint(1, 10)) # random.randint(a, b): return a random integer N such that a <= N <= b

# from import statements
from random import *

# Ending a Program Early with sys.exit()

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
