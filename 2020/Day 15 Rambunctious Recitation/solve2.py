import time


def solve(history, last_turn):
    start = time.time()
    lap = start

    # init
    num_table = {}
    for i, num in enumerate(history):
        num_table[num] = i + 1
    num_table.pop(history[-1])

    next_num = history[-1]
    first_turn = len(num_table)
    size = len(num_table)
    for turn in range(first_turn+1, last_turn):
        if next_num in num_table:
            new_next_num = turn - num_table[next_num]
        else:
            new_next_num = 0
        num_table[next_num] = turn
        next_num = new_next_num

        size += 1
        if size % 1000000 == 0:
            new_lap = time.time()
            print("{}, {}".format(new_lap - start, new_lap - lap))
            lap = new_lap

    end = time.time()
    print("{}, {}".format(end - start, end - lap))
    return next_num


if __name__ == '__main__':
    input_ = [14, 8, 16, 0, 1, 17]
    print(solve(input_, 30000000))
