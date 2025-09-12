# This program says hello and asks for my name.

print('Hello world!') #  displays the string value inside the parentheses
print('What is your name?') # ask for their name

myName = input() # waits for the user to type some text on the keyboard

print('It is good to meet you, ' + myName) 
print('The length of the your name is: ')
print(len(myName)) #  evaluates the number characters in that string
print('What is your age?')

myAge = input() # always return a string type value

print('You will be ' + str(int(myAge) + 1) + ' in a year.')