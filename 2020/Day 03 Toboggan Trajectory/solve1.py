with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

step_y = 1
step_x = 3
map_width = len(lines[0])
count_tree = 0
pos_x = step_x
for pos_y in range(step_y, len(lines), step_y):
    if lines[pos_y][pos_x % map_width] == '#':
        count_tree += 1
    pos_x += step_x

print(count_tree)
