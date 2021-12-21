def get_row_and_col(seat_id):
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

    return row, col


def get_seat_id(seat_id):
    row, col = get_row_and_col(seat_id)

    return row * 8 + col


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        ids = f.read().splitlines()
    ids.sort()

    print(get_seat_id(ids[0]))
