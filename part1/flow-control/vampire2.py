# The order of the elif statements does matter. 
name = 'Bob'
age = 3000

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000: # <- this condition is never reached
    print('Unlike you, Alice is not an undead, immortal vampire.')