
# function definition
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello() # function call

def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')

# Return Values and return Statements
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again letter'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# The None Value
spam = print('Hello')
print(None == spam)

# Keyword Arguments and print()
print('Hello')
print('World')

print('Hello', end="")
print('World')

print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep=",")

# Local and Global Scope
# Local Variables Cannot Be Used in the Global Scope
def spam():
    eggs = 31337

spam()
# print(eggs) # return error

# Local Scopes Cannot Use Variables in Other Local Scopes
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

# Global Variables Can Be Read from a Local Scope
def spam():
    print(eggs)

eggs = 42
spam()
print(eggs)

# Local and Global Variables with the Same Name
def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # 'prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'

# The global Statement
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global
spam()
print(eggs)

def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
# spam()

# Exception Handling
def spam(dividedBy):
    try:
        return 42 / dividedBy
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(spam(2))
print(spam(0))

# A Short Program: Guess the Number
import random

secreteNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secreteNumber:
        print('Your guess is too low.')
    elif guess > secreteNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!

if guess == secreteNumber:
    print('Good job! You guess my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secreteNumber))

# Practice Projects
# The Collatz Sequence
