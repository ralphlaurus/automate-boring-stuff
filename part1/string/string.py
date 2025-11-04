# Working with Strings

# String Literals
# spam = 'That is Alice\'s cat.' # escape single quote
# print(spam)
spam = "That is Alice's cat." # use double quotes
print(spam)
spam = 'Say hi to Bob\'s mother.' # escape single quote
print(spam)
# Escape Characters
print('Hello\nWorld') # \n means new line
print('Hello\tWorld') # \t means tab
print('Hello\\World') # \\ means backslash
print('Hello\'World') # \' means single quote
print('Hello\"World') # \" means double quote

# Raw Strings
print(r'That is Carol\'s cat.') # r'' means raw string, ignore escape characters

# Multiline Strings with Triple Quotes: catnapping.py
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
      
Sincerely,
Bob''')

print('Dear Alice,\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')

# Multiline Comments
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""
def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')

# Indexing and Slicing
spam = 'Hello, world!'
print(spam[0]) # H
print(spam[4]) # o
print(spam[-1]) # !
print(spam[0:5]) # Hello
print(spam[:5]) # Hello
print(spam[6:]) # world!

# Slicing a string does not modify the original string
spam = 'Hello, world!'
fizz = spam[0:5]
print(fizz) # Hello

# The in and not in Operators with Strings
print('Hello' in 'Hello, world!') # True
print('Hello' not in 'Hello, world!') # False
print('goodbye' in 'Hello, world!') # False
print('goodbye' not in 'Hello, world!') # True

# Useful String Methods

# The upper(), lower(), isupper(), and islower() Methods
spam = 'Hello, world!'
spam = spam.upper()
print(spam) # 'HELLO, WORLD!'
spam = spam.lower()
print(spam) # 'hello, world!'

# The upper() and lower() methods are helpful if you need to make a case-insensitive comparison.
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

# The isupper() and islower() methods will return a Boolean True value 
# if the string has at least one letter and all the letters are uppercase or
# lowercase, respectively. Otherwise, these methods return False.
spam = 'Hello, world!'
print(spam.islower()) # False
print(spam.isupper()) # False
print('HELLO'.isupper()) # True
print('abc12345'.islower())
print('12345'.islower()) # False, no letters
print('12345'.isupper()) # False, no letters

# Chaining Methods
print('Hello'.upper().isupper()) # True
print('Hello'.upper().lower()) # hello
print('Hello'.upper().lower().isupper()) # False

# The isX Methods

# isalpha() returns True if the string consists only of letters and is not blank.
print('Hello'.isalpha()) # True
print('Hello123'.isalpha()) # False

# isalnum() returns True if the string consists only of letters and numbers and is not blank.
print('Hello123'.isalnum()) # True
print('Hello 123'.isalnum()) # False, space is not a letter or number

# isdecimal() returns True if the string consists only of numeric characters and is not blank.
print('12345'.isdecimal()) # True
print('12345abc'.isdecimal()) # False

# isspace() returns True if the string consists only of spaces, tabs, and newlines and is not blank.
print(' \t \n'.isspace()) # True
print('  Hello  '.isspace()) # False

# isTitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.
print('Hello World'.istitle()) # True
print('Hello world'.istitle()) # False

# The isX string methods are helpful when you need to validate user input: validateInput.py
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

# The startswth() and endswith() Methods
print('Hello, world!'.startswith('Hello')) # True
print('Hello, world!'.endswith('world!')) # True

# The join() and split() Methods
print(', '.join(['cats', 'rats', 'bats'])) # cats, rats, bats
print(' '.join(['My', 'name', 'is', 'Simon'])) # My name is Simon

# Remember that join() is called on a string value and is passed a list value. 
# The split() method does the opposite: It’s called on a string value and returns a list of strings.  

print('My name is Simon'.split()) # ['My', 'name', 'is', 'Simon']
print('My name is Simon'.split('m')) # ['My na', 'e is Si', 'on']

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''

print(spam.split('\n'))
# ['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.', 'Sincerely,', 'Bob'] 

# Justify Text with rjust(), ljust(), and center()

# The rjust() and ljust() string methods return a padded version of the 
# string they are called on, with spaces inserted to justify the text.
print('Hello'.rjust(10)) #      Hello
print('Hello'.ljust(10)) # Hello     

print('Hello'.rjust(20, '*')) # ***************Hello
print('Hello'.ljust(20, '-')) # Hello---------------

# The center() string method works like ljust() and rjust() but centers
# the text rather than justifying it to the left or right.
print('Hello'.center(20)) #        Hello        
print('Hello'.center(20, '=')) # ========Hello========

# picnicTable.py
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# Removing Whitespace with strip(), rstrip(), and lstrip()
spam = '    Hello, World!    '
print(spam.strip()) # 'Hello, World!'
print(spam.lstrip()) # 'Hello, World!    '
print(spam.rstrip()) # '    Hello, World!'

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('Spam')) # 'BaconSpamEggs'
# The order of the characters in the string argument to strip() does not matter.
print(spam.lstrip('Spam')) # 'BaconSpamEggsSpamSpam'
print(spam.rstrip('Spam')) # 'SpamSpamBaconSpamEggs'

# Copying and Pasting Strings with the pyperclip Module
import pyperclip
pyperclip.copy('Hello, world!')
print(pyperclip.paste()) # Hello, world!
