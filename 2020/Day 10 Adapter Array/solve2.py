
def solve(adapters):
    DELTA = 3

    count = 0
#    print(adapters)
    if len(adapters) < 3:
        return 1
    elif adapters[1] - adapters[0] < DELTA and adapters[2] - adapters[1] < DELTA:
        count += solve(adapters[:1] + adapters[2:])
    count += solve(adapters[1:])

    return count


if __name__ == '__main__':
    DELTA = 3

    adapters = []
    with open('input.txt', 'r') as f:
        adapters = list(map(int, f.read().splitlines()))
        adapters.sort()
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + DELTA)

    patterns = []
    i = 0
    prev_index = 0
    while i < len(adapters) - 1:
        if adapters[i + 1] - adapters[i] == 3:
            patterns.append(solve(adapters[prev_index:i + 1]))
            prev_index = i + 1
        i += 1

    output = 1
#    print(patterns)
    for i in patterns:
        output *= i

    print(output)
