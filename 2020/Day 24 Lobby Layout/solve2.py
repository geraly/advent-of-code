from TileFloor import TileFloor, Color


def load_input(filename):
    with open(filename, 'r') as f:
        data = f.read().splitlines()

    steps = []
    for line in data:
        step = []
        while len(line) > 0:
            if line.startswith('se'):
                step.append('se')
                line = line[2:]
            elif line.startswith('sw'):
                step.append('sw')
                line = line[2:]
            elif line.startswith('nw'):
                step.append('nw')
                line = line[2:]
            elif line.startswith('ne'):
                step.append('ne')
                line = line[2:]
            elif line.startswith('e'):
                step.append('e')
                line = line[1:]
            elif line.startswith('w'):
                step.append('w')
                line = line[1:]
            else:
                raise("Unknown input")
        steps.append(step)

    return steps


def flip_tiles(tile_floor, steps):
    for step in steps:
        tile_floor.flip_tile(step)


if __name__ == '__main__':
    steps = load_input('input.txt')

    tile_floor = TileFloor(1000)
    flip_tiles(tile_floor, steps)

    for i in range(100):
        tile_floor.flip_tile_with_rule()

    count = tile_floor.count_tiles(Color.BLACK)
    print(count)
