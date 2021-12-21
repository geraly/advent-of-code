from CrabCups import CrabCups

if __name__ == '__main__':
    # example
    labels = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    # input
    labels = [2, 4, 7, 8, 1, 9, 3, 5, 6]
    round_num = 10000000

    labels_add = [label for label in range(len(labels)+1, 1000000+1)]
    labels += labels_add
    assert labels[-1] == 1000000
    assert len(labels) == 1000000

    crab_cups = CrabCups(labels)

    for i in range(round_num):
        if i % (round_num/10) == 0:
            print(f"--- move {i+1} ---")
        crab_cups.move()

    label1, label2 = crab_cups.get_answer2()
    print(f"label1 = {label1}, label2 = {label2}")
    print(f"answer = {label1 * label2}")
