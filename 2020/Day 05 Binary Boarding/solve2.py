def get_seat_id(seat_id):
    total_row = 128
    total_col = 8

    row = 0
    work = total_row
    for i in range(7):
        work = work >> 1
        if seat_id[i] == 'B':
            row += work

    col = 0
    work = total_col
    for i in range(3):
        work = work >> 1
        if seat_id[7+i] == 'R':
            col += work

    return row * 8 + col


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    lines.sort()

    seat_ids = list(map(get_seat_id, lines))
    seat_ids.sort()

    for i in range(seat_ids[0], seat_ids[-1]):
        if i not in seat_ids and i - 1 in seat_ids and i + 1 in seat_ids:
            print(i)
