def move(cups):
    maximum_num = max(cups)
    current_cup_label = cups[0]
    pickup = cups[1:4]
    cups = cups[0:1] + cups[4:]

    destination = current_cup_label
    while True:
        destination -= 1
        if destination < 1:
            destination = maximum_num
        if destination not in pickup:
            break

    insert_index = cups.index(destination)
    cups = cups[:insert_index+1] + pickup + cups[insert_index+1:]
    cups = cups[1:] + cups[:1]

    return cups


def shift_position(cups, number):
    target_index = cups.index(number)
    cups = cups[target_index:] + cups[:target_index]

    return cups


if __name__ == '__main__':
    # example
    cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    # input
    cups = [2, 4, 7, 8, 1, 9, 3, 5, 6]

    for i in range(100):
        print("--- move {} ---".format(i+1))
        print("cups: {}".format(" ".join(list(map(str, cups)))))
        cups = move(cups)

    print("--- final ---")
    print("cups: {}".format(" ".join(list(map(str, cups)))))

    print("--- shift position ---")
    cups = shift_position(cups, 1)
    print("cups: {}".format(" ".join(list(map(str, cups)))))

    print("--- answer ---")
    print("{}".format("".join(list(map(str, cups[1:])))))
