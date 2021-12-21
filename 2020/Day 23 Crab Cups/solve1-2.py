from CrabCups import CrabCups

if __name__ == '__main__':
    # example
    labels = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    round_num = 100
    # input
    # labels = [2, 4, 7, 8, 1, 9, 3, 5, 6]

    crab_cups = CrabCups(labels)

    for i in range(round_num):
        print(f"--- move {i+1} ---")
        cups_str = ", ".join(list(map(str, crab_cups.get_labels(i))))
        print(f"cups: {cups_str}")
        crab_cups.move()

    print("--- final ---")
    cups_str = ", ".join(list(map(str, crab_cups.get_labels(round_num))))
    print(f"cups: {cups_str}")

    print("--- answer ---")
    print(f"{crab_cups.get_answer1()}")
