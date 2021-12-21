def solve(history, last_turn):
    new_history = history.copy()
    new_history.reverse()
    last_num = new_history[0]
    first_turn = len(new_history)
    for turn in range(first_turn, last_turn):
        if last_num in new_history[1:]:
            last_trun = len(new_history) - new_history[1:].index(last_num) - 1
            last_num = turn - last_trun
            new_history.insert(0, last_num)
        else:
            new_history.insert(0, 0)
            last_num = 0

    new_history.reverse()
    return new_history


if __name__ == '__main__':

    input_ = [14, 8, 16, 0, 1, 17]

    examples = [
        [0, 3, 6],  # 0, 3, 6, 0, 3, 3, 1, 0, 4, 0
        [1, 3, 2],  # the 2020th number spoken is 1
        [2, 1, 3],  # the 2020th number spoken is 10
        [1, 2, 3],  # the 2020th number spoken is 27
        [2, 3, 1],  # the 2020th number spoken is 78
        [3, 2, 1],  # the 2020th number spoken is 438
        [3, 1, 2],  # the 2020th number spoken is 1836
    ]

    for example in examples:
        history = solve(example, 2020)
        print(history[-1])

    history = solve(input_, 2020)
    print(history[-1])
