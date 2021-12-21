def is_valid_data(xmas, data):
    for i in range(len(xmas) - 1):
        for j in range(i + 1, len(xmas)):
            if xmas[i] + xmas[j] == data:
                return True
    return False


def search_invalid_data(xmas, size):
    for i in range(size, len(xmas_data)):
        if not is_valid_data(xmas_data[i-size:i], xmas_data[i]):
            return i, xmas_data[i]

    return 0, 0


def search_weakness(xmas, data):
    for i in range(len(xmas)):
        for j in range(i, len(xmas)):
            if sum(xmas[i:j]) == data:
                return min(xmas[i:j]) + max(xmas[i:j])
            elif sum(xmas[i:j]) > data:
                break

    return 0


if __name__ == '__main__':
    xmas_data = []
    with open('input.txt', 'r') as f:
        xmas_data = list(map(int, f.read().splitlines()))

    SIZE = 25
    (index, invalid_data) = search_invalid_data(xmas_data, SIZE)
    print(search_weakness(xmas_data[:index], invalid_data))
