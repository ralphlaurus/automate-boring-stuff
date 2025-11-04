grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Print the grid in normal order
for row in grid:
    for col in row:
        print(col, end=" ")
    print()

print() # print a blank line between outputs

# Print the grid in reverse order (both rows and columns)
for row in grid:
    for col in row[::-1]:
        print(col, end=" ")
    print()

print() # print a blank line between outputs

# Print the grid rotated 90 degrees clockwise
for col in range(len(grid[0])):
    for row in range(len(grid)):
        print(grid[row][col], end=" ")
    print()

print() # print a blank line between outputs

# Print the grid rotated 90 degrees counter-clockwise
for col in range(len(grid[0]) - 1, -1, -1):
    for row in range(len(grid) - 1, -1, -1):
        print(grid[row][col], end=" ")
    print()

# To print the grid rotated 90 degrees clockwise:
# 1st: grid[0][0], grid[1][0], grid[2][0], ...
# 2nd: grid[0][1], grid[1],[1], grid[2][1], ...

# Hints: the first column should be the first row
# second column, the second row, and so on.

# Print the grid rotated 90 degrees counter-clockwise:
# 1st: grid[0][last], grid[1][last], grid[2][last], ...
# 2nd: grid[0][last-1], grid[1][last-1], grid[2][last-1], ...
# Hints: the last column should be the first row
# second-to-last column, the second row, and so on.
# To get the last index, use len(grid[0]) - 1
# To get the second-to-last index, use len(grid[0]) - 2
# To get the first index, use 0
# To get the second index, use 1
# To get the third index, use 2
# To get the last index, use -1
# To get the second-to-last index, use -2

