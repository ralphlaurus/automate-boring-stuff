print([1, 2, 3])
print(['cat', 'bat', 'rat', 'elephant'])
print(['hello', 3.1415, True, None, 42])
spam = ['cat', 'bat', 'rat', 'elephant']

# Getting Individual Values in a List with Indexes
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
print(['cat', 'bat', 'rat', 'elephant'][3])
print('Hello ' + spam[0])
print('The ' + spam[1] + ' ate the ' + spam[0] + '.')
# print(spam[1000]) # IndexError
# print(spam[1.0]) # TypeError

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1])
print(spam[1][4])

# Negative Indexes
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])
print(spam[-3])
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')

# Getting Sublist with Slices
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])

print(spam[:2])
print(spam[1:])
print(spam[:])

# Getting a List’s Length with len()
spam = ['cat', 'dog', 'moose']
print(len(spam))

# Changing Values in a List with Indexes
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
print(spam)
spam[2] = spam[1]
spam[-1] = 12345
print(spam)

# List Concatenation and List Replication
print([1, 2, 3] + ['A', 'B', 'C'])
print(['X', 'Y', 'Z'] * 3)
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

# Removing Values from Lists with del Statements
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)

# Working with Lists
catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()

    if name == '':
        break

    catNames = catNames + [name] # list concatenation

print('The cat names are: ')
for name in catNames:
    print(' ' + name)

# Using for Loops with Lists
for i in [0, 1, 2, 3]:
    print(i)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# The in and not in Operators
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
spam = ['hello', 'hi', 'howdy', 'heyas']
print('howdy' not in spam)
print('cat' not in spam)

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

# The Multiple Assignment Trick
cat = ['fat', 'black', 'loud']
size, color, disposition = cat # number of variable and length of the list must be equal

# Augmented Assignment Operators
spam = 42
spam += 1 # There are augmented assignment operators for the +, -, *, /, and % operators
print(spam)

spam = 'Hello'
spam += ' world'
print(spam)

# Methods: A method is the same thing as a function, except it is “called on” a value. 

# Finding a Value in a List with the index() Method
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))
print(spam.index('heyas'))
# print(spam.index('howdy howdy howdy')) # return a ValueError

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))

# Adding Values to Lists with the append() and insert() Methods
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)

# Removing Values from Lists with remove() 
spam = ['cat', 'dog', 'rat', 'elephant']
spam.remove('bat')
print(spam)

# spam.remove('chicken') # return ValueError

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat') # remove the first instance of the value

# del statement is good to use when you know the index of the value, the remove() method is good when you know the value.

# Sorting the Values in a List with the sort() Method
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

spam = [1, 3, 2, 4, 'Alice', 'Bob']
# spam.sort() # return TypeError

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam) #  sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings.

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower) #  sort the values in regular alphabetical order
print(spam)

# Example Program: Magic 8 Ball with a List
import random

messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

print(messages[random.randint(0, len(messages) - 1)])

# List-like Types: Strings and Tuples
name = 'Zophie'
print(name[0]) # indexing
print(name[-2]) #
print(name[0:4]) # slicing
print('Zo' in name) # in operator
print('z' in name)
print('p' not in name) # not operator

for i in name:
    print('* * * ' + i + '* * *')

# Mutable and Immutable Data Types
name = 'Zophie a cat'
# name[7] = 'the' # return TypeError

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)

eggs = [1, 2, 3]
eggs = [4, 5, 6] # this does not modify the list

eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs)

# The Tuple Data Type: immutable data type
eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
len(eggs)

# eggs[1] = 99 # return TypeError

print(type(('hello',))) # return a <class, tuple>
print(type(('hello'))) # return a <class, str>

# Converting Types with the list() and tuple() Functions
print(tuple(['cat', 'dog', 5])) # return a tuple
print(list(('cat', 'dog', 5))) # return a list
print(list('hello')) # output ['h', 'e', 'l', 'l', 'o']

# References
spam = 42
cheese = spam
spam = 100
print(spam) # output 100
print(cheese) # output 42

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(spam)
print(cheese)

# Passing References

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) # output [1, 2, 3, 'Hello']

# The copy Module’s copy() and deepcopy() Functions
import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

# If the list you need to copy contains lists, then use the copy.deepcopy() function instead of copy.copy().
