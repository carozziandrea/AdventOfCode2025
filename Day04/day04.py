def print_grid(grid):
    for line in grid:
        print(''.join(line))

def checkAdjacent(grid, r, c):
    dirs = {(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)}
    
    rows_size = len(grid)
    cols_size = len(grid[0])

    rolls = 0
    
    for dir in dirs:
        newr = r + dir[0]
        newc = c + dir[1]
        if newr < 0 or newr >= rows_size: continue
        if newc < 0 or newc >= cols_size: continue

        if grid[newr][newc] == '@': rolls += 1

    return rolls < 4

# Part 1 and 2
oldGrid = []
newGrid = []
with open('Day04/day04input.txt', 'r') as lines:
    for line in lines:
        oldGrid.append(list(line.strip()))

removedRolls = 0
currentRemovedRolls = (len(oldGrid) * len(oldGrid[0]))
first_removal = True
while currentRemovedRolls != 0:
    currentRemovedRolls = 0
    to_remove = []

    for r_index, r in enumerate(oldGrid):
        for c_index, c in enumerate(r):
            if oldGrid[r_index][c_index] != '@': continue
            if checkAdjacent(oldGrid, r_index, c_index):
                currentRemovedRolls += 1
                to_remove.append((r_index, c_index))

    for r, c in to_remove:
        oldGrid[r][c] = '.'

    if first_removal:
        print(f'Part 1: {currentRemovedRolls}')
        first_removal = False
    removedRolls += currentRemovedRolls

print(f'Part 2: {removedRolls}')