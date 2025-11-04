# File and File Paths
# - A file has two key properties: a filename (usually written as one word) and a path.

# Backslash on Windows and Forward Slash on OS X and Linux
import os

print(os.path.join('usr', 'bin', 'spam')) # The os.path.join() function is helpful 
# if you need to create strings for filenames.

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in myFiles:
    print(os.path.join('C:\\User\\asweigart', filename))

# The Current Working Directory

print(os.getcwd())
os.chdir('C:\\Windows\\System32')
print(os.getcwd())

# os.chdir('C:\\ThisFolderDoesNotExist') # Error

# Absolute vs. Relative Paths
# - An absolute path, which always begins with the root folder
# - A relative path, which is relative to the program’s current working directory

"""
There are also the dot (.) and dot-dot (..) folders. These are not real 
folders but special names that can be used in a path. A single period (“dot”) 
for a folder name is shorthand for “this directory.” Two periods (“dot-dot”) 
means “the parent folder
"""

# Creating New Folders with os.makedirs()
# os.makedirs('C:\\delicious\\walnut\\waffles') # Throw error if folder already exists

# The os.path Module

# Handling Absolute and Relative Paths
"""
•    Calling os.path.abspath(path) will return a string of the absolute path 
     of the argument. This is an easy way to convert a relative path into an absolute one.
•	 Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.
•	 Calling os.path.relpath(path, start) will return a string of a relative path 
from the start path to path. If start is not provided, the current working 
directory is used as the start path.
"""
print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))

print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
print( os.getcwd())

"""
Calling os.path.dirname(path) will return a string of everything that comes 
before the last slash in the path argument. Calling os.path.basename(path) will 
return a string of everything that comes after the last slash in the path argument.
"""
path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
print(os.path.dirname(path))

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(calcFilePath)) # get dir name and base name together

print(calcFilePath.split(os.path.sep))