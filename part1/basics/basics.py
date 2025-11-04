# Entering Expressions into the Interactive Shell
print(2 + 2) # expression consist of values and an operator

# Math Operators from Highest to Lowest Precedence
print(2 ** 3) # Exponent
print(22 % 8) # Modulus/Remainder
print(22 // 8) # Floor Division
print(22 / 8) # Division
print(2 * 3) # Multiplication
print(2 + 3) # Addition
print(3 - 2) # Subtraction

# The Integer, Floating-Point, and String Data Types

# Integer -2, -1, 0, 1, 2, 3...
# Floating-Point -1.25, -1.0, 0.0, 1.0, 1.25...
# String 'a', 'aa', 'aaa', 'Hello!', '11 cats'

# String Concatenation and Replication

print('Alice' + 'Bob') # Concatenation
print('Alice ' * 5) # Replication

# Storing Values in Variables
spam = 42 # assignment statement
print(spam)

eggs = 2
print(spam + eggs)

print(spam + eggs + spam)
spam = spam + 2

print(spam)

# Variable Names

# i. Can be only one word
# ii. Can use only letter, numbers, and the underscore(_) character
# iii. Can't begin with number
# 
# Examples: balance, currentBalance, current_balance, _spam, SPAM, account4 

# The str(), int(), and float() Functions
print('I am ' + str(29) + ' years old.') # get the string type of 29 value
# Examples: str(0), str(-3.14), int('42'), int('-99'), int(1.25), int(1.99), float('3.14'), float(10)

# Text and Number Equivalence
print(42 == '42') # False
print(42 == 42.0) # True
print(42.0 == 0042.000) # True

# Extra credit: search for python documentation for len() function in built-in functions, skim the list of other functions python has, like round() function, experiment with it in the interactive shell.
