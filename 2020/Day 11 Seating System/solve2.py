import copy

FLOOR = '.'
EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'


def get_next_layout(layout, width, height):
    next_layout = copy.deepcopy(layout)

    for y in range(height):
        for x in range(width):
            if layout[y][x] == FLOOR:
                continue

            count_occupied_seat = 0
            # remember ten key layout
            # 789
            # 4 6
            # 123
            # 1
            for yy, xx in zip(range(y+1, height), range(x-1, -1, -1)):
                if layout[yy][xx] == OCCUPIED_SEAT:
                    count_occupied_seat += 1
                    break
                elif layout[yy][xx] == EMPTY_SEAT:
                    break
            # 2
            for yy in range(y+1, height):
                if layout[yy][x] == OCCUPIED_SEAT:
                    count_occupied_seat += 1
                    break
                elif layout[yy][x] == EMPTY_SEAT:
                    break
            # 3
            for yy, xx in zip(range(y+1, height), range(x+1, width)):
                if layout[yy][xx] == OCCUPIED_SEAT:
                    count_occupied_seat += 1
                    break
                elif layout[yy][xx] == EMPTY_SEAT:
                    break
            # 4
            for xx in range(x-1, -1, -1):
                if layout[y][xx] == OCCUPIED_SEAT:
                    count_occupied_seat += 1
                    break
                elif layout[y][xx] == EMPTY_SEAT:
                    break
            # 6
            for xx in range(x+1, width):
                if layout[y][xx] == OCCUPIED_SEAT:
                    count_occupied_seat += 1
                    break
                elif layout[y][xx] == EMPTY_SEAT:
                    break
            # 7
            for yy, xx in zip(range(y-1, -1, -1), range(x-1, -1, -1)):
                if layout[yy][xx] == OCCUPIED_SEAT:
                    count_occupied_seat += 1
                    break
                elif layout[yy][xx] == EMPTY_SEAT:
                    break
            # 8
            for yy in range(y-1, -1, -1):
                if layout[yy][x] == OCCUPIED_SEAT:
                    count_occupied_seat += 1
                    break
                elif layout[yy][x] == EMPTY_SEAT:
                    break
            # 9
            for yy, xx in zip(range(y-1, -1, -1), range(x+1, width)):
                if layout[yy][xx] == OCCUPIED_SEAT:
                    count_occupied_seat += 1
                    break
                elif layout[yy][xx] == EMPTY_SEAT:
                    break

            if layout[y][x] == EMPTY_SEAT and 8 - count_occupied_seat == 8:
                next_layout[y][x] = OCCUPIED_SEAT
            elif layout[y][x] == OCCUPIED_SEAT and count_occupied_seat >= 5:
                next_layout[y][x] = EMPTY_SEAT

    return next_layout


def is_stabilized(layout1, layout2):
    for line1, line2 in zip(layout1, layout2):
        for s1, s2 in zip(line1, line2):
            if s1 != s2:
                return False

    return True


def print_layout(layout):
    for line in layout:
        print(''.join(line))
    print()


if __name__ == '__main__':

    layout = []
    with open('input.txt', 'r') as f:
        layout = list(map(list, f.read().splitlines()))

    width = len(layout[0])
    height = len(layout)

#    print_layout(layout)
    while True:
        next_layout = get_next_layout(layout, width, height)
#        print_layout(next_layout)
        if is_stabilized(layout, next_layout):
            break
        layout = next_layout

    count_occupied_seat = 0
    for line in next_layout:
        for s in line:
            if s == OCCUPIED_SEAT:
                count_occupied_seat += 1

    print(count_occupied_seat)
