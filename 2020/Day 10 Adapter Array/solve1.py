
if __name__ == '__main__':
    DELTA = 3

    adapters = []
    with open('input.txt', 'r') as f:
        adapters = list(map(int, f.read().splitlines()))
        adapters.sort()
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + DELTA)

    diff_count = {}
    for i in range(1, DELTA+1):
        diff_count[i] = 0

    i = 0
    while i < len(adapters) - 1:
        difference = adapters[i + 1] - adapters[i]
        diff_count[difference] += 1
        i += 1

    for jolt, count in diff_count.items():
        if count > 0:
            print("{} differences of {} jolt".format(count, jolt))

    print(diff_count[1] * diff_count[3])
