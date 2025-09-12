

passwordFile = open('SecretePasswordsFile.txt')
secretePassword = passwordFile.read()
print('Enter your password: ')
typedPassword = input()
if typedPassword == secretePassword:
    print('Access Granted')
    if typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access Denied')