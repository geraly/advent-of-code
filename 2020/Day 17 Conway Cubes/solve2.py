import copy

CYCLE = 6
ACTIVE = '#'
INACTIVE = '.'


def count_active_nighbor(space, x, y, z, w):
    count = 0
    for xx in range(x-1, x+2):
        for yy in range(y-1, y+2):
            for zz in range(z-1, z+2):
                for ww in range(w-1, w+2):
                    if space[xx][yy][zz][ww] == ACTIVE:
                        count += 1

    if space[x][y][z][w] == ACTIVE:
        count -= 1

    return count


def do_one_cycle(space, space_x, space_y, space_z, space_w):
    next_space = copy.deepcopy(space)

    for x in range(1, space_x-1):
        for y in range(1, space_y-1):
            for z in range(1, space_z-1):
                for w in range(1, space_w-1):
                    active_nighbor_num = count_active_nighbor(
                        space, x, y, z, w)

                    if space[x][y][z][w] == ACTIVE:
                        if active_nighbor_num == 2 or active_nighbor_num == 3:
                            pass
                        else:
                            next_space[x][y][z][w] = INACTIVE
                    else:
                        if active_nighbor_num == 3:
                            next_space[x][y][z][w] = ACTIVE

    return next_space


def count_active_cube(space, space_x, space_y, space_z, space_w):
    count = 0
    for x in range(space_x):
        for y in range(space_y):
            for z in range(space_z):
                for w in range(space_w):
                    if space[x][y][z][w] == ACTIVE:
                        count += 1

    return count


if __name__ == '__main__':
    SPACE_Z = (CYCLE + 1) * 2 + 1
    SPACE_W = SPACE_Z

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        input_height = len(lines)
        input_width = len(lines[0])
        SPACE_X = (CYCLE + 1) * 2 + input_width
        SPACE_Y = (CYCLE + 1) * 2 + input_height
        space = [[[[INACTIVE for w in range(SPACE_W)] for z in range(
            SPACE_Z)] for y in range(SPACE_Y)] for x in range(SPACE_X)]

        y = CYCLE + 1
        for line in lines:
            x = CYCLE + 1
            for cube in line:
                space[x][y][CYCLE+1][CYCLE+1] = cube
                x += 1
            y += 1

    for i in range(1, CYCLE+1):
        space = do_one_cycle(space, SPACE_X, SPACE_Y, SPACE_Z, SPACE_W)

    print(count_active_cube(space, SPACE_X, SPACE_Y, SPACE_Z, SPACE_W))
