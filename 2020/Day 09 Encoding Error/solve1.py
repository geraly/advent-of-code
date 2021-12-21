def is_valid_data(xmas, data):

    for i in range(len(xmas) - 1):
        for j in range(i + 1, len(xmas)):
            if xmas[i] + xmas[j] == data:
                return True
    return False


if __name__ == '__main__':
    xmas_data = []
    with open('input.txt', 'r') as f:
        xmas_data = list(map(int, f.read().splitlines()))

    size = 25
    for i in range(size, len(xmas_data)):
        if not is_valid_data(xmas_data[i-size:i], xmas_data[i]):
            print(xmas_data[i])
            break
