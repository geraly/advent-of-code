data = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    data = [int(d) for d in lines]

while len(data) >= 2:
    x = data.pop(0)
    for y in data:
        if x + y == 2020:
            print("{} * {} = {}".format(x, y, x*y))
