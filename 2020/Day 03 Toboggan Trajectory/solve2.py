def traverse(step_x, step_y, map_lines, map_width):
    count_tree = 0
    pos_x = step_x
    for pos_y in range(step_y, len(map_lines), step_y):
        if map_lines[pos_y][pos_x % map_width] == '#':
            count_tree += 1
        pos_x += step_x

    return count_tree


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        map_lines = f.read().splitlines()
    map_width = len(map_lines[0])

    output = 1
    tree_count = traverse(1, 1, map_lines, map_width)
    print(tree_count)
    output *= tree_count

    tree_count = traverse(3, 1, map_lines, map_width)
    print(tree_count)
    output *= tree_count

    tree_count = traverse(5, 1, map_lines, map_width)
    print(tree_count)
    output *= tree_count

    tree_count = traverse(7, 1, map_lines, map_width)
    print(tree_count)
    output *= tree_count

    tree_count = traverse(1, 2, map_lines, map_width)
    print(tree_count)
    output *= tree_count

    print(output)
