from functools import reduce

# 中国剰余定理 (CRT) の解説と、それを用いる問題のまとめ
# https://qiita.com/drken/items/ae02240cd1f8edfc86fd

# 中国人剰余定理
# https://tex2e.github.io/blog/crypto/crt


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def chinese_remainder(a, n):
    # a := [a1, a2, ..., ak]
    # n := [n1, n2, ..., nk]
    total = 0
    prod = reduce(lambda x, y: x*y, n)
    for n_i, a_i in zip(n, a):
        b_i = prod // n_i
        total += a_i * b_i * modinv(b_i, n_i)
    return total % prod


def solve(bus_ids):
    # remove 'x', calc indexes
    bus_indexes = []
    bus_ids_x_removed = []
    for index, id_ in enumerate(bus_ids):
        if id_ == 'x':
            continue
        bus_indexes.append(index)
        bus_ids_x_removed.append(int(id_))

    mods = [id_ - index for index, id_ in zip(bus_indexes, bus_ids_x_removed)]

    a = chinese_remainder(mods, bus_ids_x_removed)

    return a


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        bus_ids = [i for i in lines[1].split(',')]

    # debug
    example1 = ['7', '13', 'x', 'x', '59', 'x', '31', '19']  # 1068781
    example2 = ['17', 'x', '13', '19']  # 3417
    example3 = ['67', '7', '59', '61']  # 754018
    example4 = ['67', 'x', '7', '59', '61']  # 779210
    example5 = ['67', '7', 'x', '59', '61']  # 1261476
    example6 = ['1789', '37', '47', '1889']  # 1202161486
    example7 = ['x', 'x', '3', '5']

    target = [example1, example2, example3, example4,
              example5, example6, example7, bus_ids]

    for i, e in enumerate(target):
        print("{}, {}".format(i, solve(e)))
