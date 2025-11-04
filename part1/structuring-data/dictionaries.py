# The Dictionary Data Type
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print(myCat['size'])

print('My cat has ' + myCat['color'] + ' fur.')

spam = {12345: 'Luggage Combination', 42: 'The Answer'}

# Dictionaries vs. Lists 
# Items in dictionaries are unordered, while items in lists are ordered.
# In lists, the order of items matters, but in dictionaries, it does not.
# Lists use integer indexes to access values, while dictionaries use keys of any immutable data type (string, integer, tuple).
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon) # False

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}

print(eggs == ham) # True

spam = {'name': 'Zophie', 'age': 7}
# print(spam['color']) # return KeyError

# birthdays.py
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

# The keys(), values(), and items() Methods
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

spam = {'color': 'red', 'age': 42}
print(spam.keys())
print(list(spam.keys()))

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + k + 'Value: ' + str(v))

# Checking Whether a Key or Value Exists in a Dictionary
spam = {'name': 'Zophie', 'age': 7} 
print('name' in spam.keys())
print('Zophie' in spam.keys())
print('color' in spam.keys())
print('color' not in spam.keys())
print('color' in spam) # same as 'color' in spam.keys()

# The get() Method
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print( 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# The setdefault() Method
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black') # will add 'color' key with value 'black'
print(spam)
spam.setdefault('color', 'white') # will not change the value of 'color' key
print(spam)

# Character Count: characterCount.py
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0) # setdefault() will add the key with value 0 if the key does not exist
    count[character] = count[character] + 1 # count[character] += 1

print(count)

# Pretty Printing: prettyCharacterCount.py
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

# Using Data Structures to Model Real-World Things

# Tic Tac Toe: ticTacToe.py
theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)

# Nested Dictionaries and Lists
allGuests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies    ' + str(totalBrought(allGuests, 'apple pies')))

# Lists in Dictionaries: movies.py
movies = {
    'The Holy Grail': 1975,
    'The Life of Brian': 1979,
    'The Meaning of Life': 1983
    }

for k, v in movies.items():
    print(k + ' came out in ' + str(v))

movies['Monty Python and the Holy Grail'] = 1975
print(movies)

# Lists of Dictionaries: people.py
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}, 
    {'name': 'Charlie', 'age': 35}
]

for person in people:
    print(person['name'] + ' is ' + str(person['age']) + ' years old.')

print(people[1]['name'] + ' is ' + str(people[1]['age']) + ' years old.')

