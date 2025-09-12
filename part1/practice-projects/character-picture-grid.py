grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(len(grid)):
    print(grid[x][0])

    for y in range(len(grid[x])):
        print(grid[x][y], end="")
        
    # print()


# 1st: grid[0][0], grid[1][0], grid[2][0], ...
# 2nd: grid[0][1], grid[1],[1], grid[2][1], ...

# Hints: the first column should be the first row
# second column, the second row, and so on.