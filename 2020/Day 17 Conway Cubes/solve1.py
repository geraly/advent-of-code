import copy

CYCLE = 6
ACTIVE = '#'
INACTIVE = '.'


def show_space(space, space_x, space_y, space_z, cycle, handle,
               skip_inactive_z=True):
    output_buf = ""
    for z in range(space_z):

        is_all_inactive = True
        if skip_inactive_z:
            for yy in range(space_x):
                for xx in range(space_y):
                    if space[xx][yy][z] == ACTIVE:
                        is_all_inactive = False
                        break
                    if not is_all_inactive:
                        break
            if is_all_inactive:
                continue
        output_buf += "z = {}\n".format(z-cycle-1)
        for y in range(space_x):
            for x in range(space_y):
                output_buf += space[x][y][z]
            output_buf += "\n"

    handle.write(output_buf)


def do_one_cycle(space, space_x, space_y, space_z):
    next_space = copy.deepcopy(space)

    for x in range(1, space_x-1):
        for y in range(1, space_y-1):
            for z in range(1, space_z-1):
                count_active_nighbor = 0
                if space[x-1][y-1][z-1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x-1][y-1][z] == ACTIVE:
                    count_active_nighbor += 1
                if space[x-1][y-1][z+1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x-1][y][z-1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x-1][y][z] == ACTIVE:
                    count_active_nighbor += 1
                if space[x-1][y][z+1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x-1][y+1][z-1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x-1][y+1][z] == ACTIVE:
                    count_active_nighbor += 1
                if space[x-1][y+1][z+1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x][y-1][z-1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x][y-1][z] == ACTIVE:
                    count_active_nighbor += 1
                if space[x][y-1][z+1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x][y][z-1] == ACTIVE:
                    count_active_nighbor += 1
#                if space[x][y][z] == ACTIVE:
#                    count_active_nighbor += 1
                if space[x][y][z+1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x][y+1][z-1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x][y+1][z] == ACTIVE:
                    count_active_nighbor += 1
                if space[x][y+1][z+1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x+1][y-1][z-1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x+1][y-1][z] == ACTIVE:
                    count_active_nighbor += 1
                if space[x+1][y-1][z+1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x+1][y][z-1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x+1][y][z] == ACTIVE:
                    count_active_nighbor += 1
                if space[x+1][y][z+1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x+1][y+1][z-1] == ACTIVE:
                    count_active_nighbor += 1
                if space[x+1][y+1][z] == ACTIVE:
                    count_active_nighbor += 1
                if space[x+1][y+1][z+1] == ACTIVE:
                    count_active_nighbor += 1

                if space[x][y][z] == ACTIVE:
                    if count_active_nighbor == 2 or count_active_nighbor == 3:
                        pass
                    else:
                        next_space[x][y][z] = INACTIVE
                else:
                    if count_active_nighbor == 3:
                        next_space[x][y][z] = ACTIVE

    return next_space


def count_active_cube(space, space_x, space_y, space_z):
    count = 0
    for x in range(space_x):
        for y in range(space_y):
            for z in range(space_z):
                if space[x][y][z] == ACTIVE:
                    count += 1

    return count


if __name__ == '__main__':
    SPACE_Z = (CYCLE + 1) * 2 + 1

    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        input_height = len(lines)
        input_width = len(lines[0])
        SPACE_X = (CYCLE + 1) * 2 + input_width
        SPACE_Y = (CYCLE + 1) * 2 + input_height
        space = [[[INACTIVE for z in range(SPACE_Z)]
                  for y in range(SPACE_Y)] for x in range(SPACE_X)]

        y = CYCLE + 1
        for line in lines:
            x = CYCLE + 1
            for cube in line:
                space[x][y][CYCLE+1] = cube
                x += 1
            y += 1

    f = open("output.txt", "w")

    show_space(space, SPACE_X, SPACE_Y, SPACE_Z, CYCLE, f)
    for i in range(1, CYCLE+1):
        space = do_one_cycle(space, SPACE_X, SPACE_Y, SPACE_Z)
        f.write("cycle = {}\n".format(i))
        show_space(space, SPACE_X, SPACE_Y, SPACE_Z, CYCLE, f)
    f.close()

    print(count_active_cube(space, SPACE_X, SPACE_Y, SPACE_Z))
