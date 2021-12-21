import copy

FLOOR = '.'
EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'


def get_next_layout(layout, width, height):
    next_layout = copy.deepcopy(layout)

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if layout[y][x] == FLOOR:
                continue

            count_occupied_seat = 0
            if layout[y+1][x-1] == OCCUPIED_SEAT:
                count_occupied_seat += 1
            if layout[y+1][x] == OCCUPIED_SEAT:
                count_occupied_seat += 1
            if layout[y+1][x+1] == OCCUPIED_SEAT:
                count_occupied_seat += 1
            if layout[y][x-1] == OCCUPIED_SEAT:
                count_occupied_seat += 1
            if layout[y][x+1] == OCCUPIED_SEAT:
                count_occupied_seat += 1
            if layout[y-1][x-1] == OCCUPIED_SEAT:
                count_occupied_seat += 1
            if layout[y-1][x] == OCCUPIED_SEAT:
                count_occupied_seat += 1
            if layout[y-1][x+1] == OCCUPIED_SEAT:
                count_occupied_seat += 1

            if layout[y][x] == EMPTY_SEAT and 8 - count_occupied_seat == 8:
                next_layout[y][x] = OCCUPIED_SEAT
            elif layout[y][x] == OCCUPIED_SEAT and count_occupied_seat >= 4:
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
        layout = f.read().splitlines()

    # expand floor
    for i in range(len(layout)):
        layout[i] = list(FLOOR + layout[i] + FLOOR)
    empty_line = [FLOOR for x in range(len(layout[0]))]
    layout.insert(0, empty_line)
    layout.append(empty_line)

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
