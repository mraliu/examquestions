grid = ['T','O','P','S','E']

x = 3

print(grid)

grid[x] = grid[0]
grid[0] = grid[x-1]

print(grid)