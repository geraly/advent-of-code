if __name__ == '__main__':

    layout = []
    with open('input.txt', 'r') as f:
        instructions = f.read().splitlines()

    #   N
    # W   E
    #   S
    #   latitude + 1 is move south
    #   longitude + 1 is move east
    latitude = 0
    longitude = 0
    # 0: E
    # 1: N
    # 2: W
    # 3: S
    direction = 0
    for line in instructions:
        action = line[0]
        value = int(line[1:])

        if action == 'E':
            longitude += value
        elif action == 'W':
            longitude -= value
        elif action == 'S':
            latitude += value
        elif action == 'N':
            latitude -= value
        elif action == 'L':
            direction = (direction + (value / 90)) % 4
        elif action == 'R':
            direction = (direction - (value / 90)) % 4
        elif action == 'F':
            if direction == 0:
                longitude += value
            elif direction == 1:
                latitude -= value
            elif direction == 2:
                longitude -= value
            elif direction == 3:
                latitude += value

    print(abs(latitude) + abs(longitude))
