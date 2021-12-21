def rotate_waypoint_90(x, y):
    return -y, x


if __name__ == '__main__':

    layout = []
    with open('input.txt', 'r') as f:
        instructions = f.read().splitlines()

    #   N
    # W   E
    #   S
    #   ship_latitude + 1 is move south
    #   ship_longitude + 1 is move east
    ship_latitude = 0
    ship_longitude = 0
    waypoint_latitude = -1
    waypoint_longitude = 10
    for line in instructions:
        action = line[0]
        value = int(line[1:])

        if action == 'E':
            waypoint_longitude += value
        elif action == 'W':
            waypoint_longitude -= value
        elif action == 'S':
            waypoint_latitude += value
        elif action == 'N':
            waypoint_latitude -= value
        elif action == 'L':
            for i in range(int(-value / 90) % 4):
                waypoint_longitude, waypoint_latitude = rotate_waypoint_90(
                    waypoint_longitude, waypoint_latitude)
        elif action == 'R':
            for i in range(int(value / 90) % 4):
                waypoint_longitude, waypoint_latitude = rotate_waypoint_90(
                    waypoint_longitude, waypoint_latitude)
        elif action == 'F':
            ship_longitude += waypoint_longitude * value
            ship_latitude += waypoint_latitude * value

    print(abs(ship_latitude) + abs(ship_longitude))
