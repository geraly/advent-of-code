data = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    data = [int(d) for d in lines]

for i, x in enumerate(data):
    for j, y in enumerate(data[i+1:]):
        for z in data[j+1:]:
            if x + y + z == 2020:
                print("{} * {} * {} = {}".format(x, y, z, x*y*z))
