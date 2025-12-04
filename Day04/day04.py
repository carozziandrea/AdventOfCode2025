def should_be_removed(grid, r, c):
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)]

    rows_size = len(grid)
    cols_size = len(grid[0])

    neighbor_count = 0

    for dr, dc in dirs:
        newr, newc = r + dr, c + dc
        if 0 <= newr < rows_size and 0 <= newc < cols_size:
            if grid[newr][newc] == '@':
                neighbor_count += 1
                if neighbor_count >= 4:
                    return False

    return True

# Part 1 and 2
with open('Day04/day04input.txt', 'r') as f:
    grid = [list(line.strip()) for line in f]

removedRolls = 0
currentRemovedRolls = 1
first_removal = True

while currentRemovedRolls != 0:
    currentRemovedRolls = 0
    to_remove = []

    for r_index, row in enumerate(grid):
        for c_index, cell in enumerate(row):
            if cell != '@': continue
            if should_be_removed(grid, r_index, c_index):
                currentRemovedRolls += 1
                to_remove.append((r_index, c_index))

    for r, c in to_remove:
        grid[r][c] = '.'

    if first_removal:
        print(f'Part 1: {currentRemovedRolls}')
        first_removal = False
    removedRolls += currentRemovedRolls

print(f'Part 2: {removedRolls}')