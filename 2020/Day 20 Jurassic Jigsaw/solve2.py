import math

RIGHT = "right"
TOP = "top"
LEFT = "left"
BOTTOM = "bottom"
DATA = "data"

MONSTER = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' '],
    ['#', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ',
        ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#'],
    [' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ',
        '#', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' '],
]


def get_edges(tile_data):
    #   1
    # 2   0
    #   3
    edge0 = []
    edge2 = []
    for i in range(len(tile_data)):
        edge0.append(tile_data[i][-1])
        edge2.append(tile_data[i][0])

    edges = {
        RIGHT: ''.join(edge0),
        TOP: tile_data[0],
        LEFT: ''.join(edge2),
        BOTTOM: tile_data[-1],
    }

    return edges


def search_neighbor_edge(tile1, tile2):
    """search neighbor edge

    Args:
        tile1: tile1
        tile2: tile2

    Returns:
        direction1, direction2, reverse:
            direction1, direction2: RIGHT, TOP, LEFT, BOTTOM
            reverse: True or False
            if tile1 is not neighbor tile2, return None, None, None
    """
    edges1 = get_edges(tile1)
    edges2 = get_edges(tile2)

    for dir1, data1 in edges1.items():
        for dir2, data2 in edges2.items():
            if data1 == data2:
                return dir1, dir2, False
            if data1 == data2[::-1]:
                return dir1, dir2, True

    return None, None, None


def flip_vertical(tile):
    tile[DATA] = tile[DATA][::-1]
    temp = tile[TOP]
    tile[TOP] = tile[BOTTOM]
    tile[BOTTOM] = temp
    return tile


def flip_horizontal(tile):
    ret_tile_data = [None for i in range(len(tile[DATA]))]
    for i in range(len(tile[DATA])):
        ret_tile_data[i] = tile[DATA][i][::-1]

    tile[DATA] = ret_tile_data
    temp = tile[LEFT]
    tile[LEFT] = tile[RIGHT]
    tile[RIGHT] = temp

    return tile


def rotate(tile, direction=LEFT):
    """rotate tile data

    Args:
        tile_data: tile data
        direction (RIGHT or LEFT): RIGHT is clockwise, LEFT is Counterclockwise

    Returns:
        tile_data: rotated tile data
    """

    ret_tile_data = ['' for i in range(len(tile[DATA]))]
    for i in range(len(tile[DATA])):
        for j in range(len(tile[DATA])):
            if direction == LEFT:
                ret_tile_data[-j-1] += tile[DATA][i][j]
            elif direction == RIGHT:
                ret_tile_data[j] += tile[DATA][len(tile[DATA])-i-1][j]

    tile[DATA] = ret_tile_data
    if direction == LEFT:
        temp = tile[BOTTOM]
        tile[BOTTOM] = tile[RIGHT]
        tile[RIGHT] = tile[TOP]
        tile[TOP] = tile[LEFT]
        tile[LEFT] = temp
    else:
        temp = tile[BOTTOM]
        tile[BOTTOM] = tile[LEFT]
        tile[LEFT] = tile[TOP]
        tile[TOP] = tile[RIGHT]
        tile[RIGHT] = temp

    return tile


def arrange_tiles(tiles):
    remaining_tiles = list(tiles.items())
    while len(remaining_tiles) > 0:
        tile1_id, tile1_val = remaining_tiles.pop(0)
        found_directions_count = 0
        if tile1_val[RIGHT] is not None:
            found_directions_count += 1
        if tile1_val[TOP] is not None:
            found_directions_count += 1
        if tile1_val[LEFT] is not None:
            found_directions_count += 1
        if tile1_val[BOTTOM] is not None:
            found_directions_count += 1

        arranged_tiles = []
        for tile2_id, tile2_val in remaining_tiles:
            if found_directions_count == 4:
                break
            dir1, dir2, is_reverse = search_neighbor_edge(
                tile1_val[DATA], tile2_val[DATA])
            if dir1 is None:
                continue

            if dir1 == RIGHT and dir2 == RIGHT:
                tiles[tile2_id] = flip_horizontal(tiles[tile2_id])
                if is_reverse:
                    tiles[tile2_id] = flip_vertical(tiles[tile2_id])
                tiles[tile1_id][RIGHT] = tile2_id
                tiles[tile2_id][LEFT] = tile1_id
            elif dir1 == RIGHT and dir2 == TOP:
                tiles[tile2_id] = rotate(tiles[tile2_id])
                if not is_reverse:
                    tiles[tile2_id] = flip_vertical(tiles[tile2_id])
                tiles[tile1_id][RIGHT] = tile2_id
                tiles[tile2_id][LEFT] = tile1_id
            elif dir1 == RIGHT and dir2 == LEFT:
                if is_reverse:
                    tiles[tile2_id] = flip_vertical(tiles[tile2_id])
                tiles[tile1_id][RIGHT] = tile2_id
                tiles[tile2_id][LEFT] = tile1_id
            elif dir1 == RIGHT and dir2 == BOTTOM:
                tiles[tile2_id] = rotate(tiles[tile2_id], RIGHT)
                if is_reverse:
                    tiles[tile2_id] = flip_vertical(tiles[tile2_id])
                tiles[tile1_id][RIGHT] = tile2_id
                tiles[tile2_id][LEFT] = tile1_id
            elif dir1 == TOP and dir2 == RIGHT:
                tiles[tile2_id] = rotate(tiles[tile2_id], RIGHT)
                if not is_reverse:
                    tiles[tile2_id] = flip_horizontal(tiles[tile2_id])
                tiles[tile1_id][TOP] = tile2_id
                tiles[tile2_id][BOTTOM] = tile1_id
            elif dir1 == TOP and dir2 == TOP:
                tiles[tile2_id] = flip_vertical(tiles[tile2_id])
                if is_reverse:
                    tiles[tile2_id] = flip_horizontal(tiles[tile2_id])
                tiles[tile1_id][TOP] = tile2_id
                tiles[tile2_id][BOTTOM] = tile1_id
            elif dir1 == TOP and dir2 == LEFT:
                tiles[tile2_id] = rotate(tiles[tile2_id], LEFT)
                if is_reverse:
                    tiles[tile2_id] = flip_horizontal(tiles[tile2_id])
                tiles[tile1_id][TOP] = tile2_id
                tiles[tile2_id][BOTTOM] = tile1_id
            elif dir1 == TOP and dir2 == BOTTOM:
                if is_reverse:
                    tiles[tile2_id] = flip_horizontal(tiles[tile2_id])
                tiles[tile1_id][TOP] = tile2_id
                tiles[tile2_id][BOTTOM] = tile1_id
            elif dir1 == LEFT and dir2 == RIGHT:
                if is_reverse:
                    tiles[tile2_id] = flip_vertical(tiles[tile2_id])
                tiles[tile1_id][LEFT] = tile2_id
                tiles[tile2_id][RIGHT] = tile1_id
            elif dir1 == LEFT and dir2 == TOP:
                tiles[tile2_id] = rotate(tiles[tile2_id], RIGHT)
                if is_reverse:
                    tiles[tile2_id] = flip_vertical(tiles[tile2_id])
                tiles[tile1_id][LEFT] = tile2_id
                tiles[tile2_id][RIGHT] = tile1_id
            elif dir1 == LEFT and dir2 == LEFT:
                tiles[tile2_id] = flip_horizontal(tiles[tile2_id])
                if is_reverse:
                    tiles[tile2_id] = flip_vertical(tiles[tile2_id])
                tiles[tile1_id][LEFT] = tile2_id
                tiles[tile2_id][RIGHT] = tile1_id
            elif dir1 == LEFT and dir2 == BOTTOM:
                tiles[tile2_id] = rotate(tiles[tile2_id], LEFT)
                if not is_reverse:
                    tiles[tile2_id] = flip_vertical(tiles[tile2_id])
                tiles[tile1_id][LEFT] = tile2_id
                tiles[tile2_id][RIGHT] = tile1_id
            elif dir1 == BOTTOM and dir2 == RIGHT:
                tiles[tile2_id] = rotate(tiles[tile2_id], LEFT)
                if is_reverse:
                    tiles[tile2_id] = flip_horizontal(tiles[tile2_id])
                tiles[tile1_id][BOTTOM] = tile2_id
                tiles[tile2_id][TOP] = tile1_id
            elif dir1 == BOTTOM and dir2 == TOP:
                if is_reverse:
                    tiles[tile2_id] = flip_horizontal(tiles[tile2_id])
                tiles[tile1_id][BOTTOM] = tile2_id
                tiles[tile2_id][TOP] = tile1_id
            elif dir1 == BOTTOM and dir2 == LEFT:
                tiles[tile2_id] = rotate(tiles[tile2_id], RIGHT)
                if not is_reverse:
                    tiles[tile2_id] = flip_horizontal(tiles[tile2_id])
                tiles[tile1_id][BOTTOM] = tile2_id
                tiles[tile2_id][TOP] = tile1_id
            elif dir1 == BOTTOM and dir2 == BOTTOM:
                tiles[tile2_id] = flip_vertical(tiles[tile2_id])
                if is_reverse:
                    tiles[tile2_id] = flip_horizontal(tiles[tile2_id])
                tiles[tile1_id][BOTTOM] = tile2_id
                tiles[tile2_id][TOP] = tile1_id
            arranged_tiles.append((tile2_id, tile2_val))
        for item_ in arranged_tiles:
            remaining_tiles.remove(item_)
            remaining_tiles.insert(0, item_)
    return tiles


def restore_image_array(tiles):
    image_size = math.isqrt(len(tiles))
    image = [[] for i in range(image_size)]

    # search left-top
    left_top_tile_id = list(tiles.keys())[0]
    while tiles[left_top_tile_id][LEFT] is not None:
        left_top_tile_id = tiles[left_top_tile_id][LEFT]
    while tiles[left_top_tile_id][TOP] is not None:
        left_top_tile_id = tiles[left_top_tile_id][TOP]

    for i in range(len(image)):
        current_tile_id = left_top_tile_id
        for j in range(i):
            current_tile_id = tiles[current_tile_id][BOTTOM]
        for j in range(len(image)):
            image[i].append(current_tile_id)
            current_tile_id = tiles[current_tile_id][RIGHT]
        assert current_tile_id is None

    return image


def restore_image(tiles):
    tiles = arrange_tiles(tiles)
    image_array = restore_image_array(tiles)
    tile_size = len(list(tiles.values())[0][DATA])
    image_size = len(image_array) * (tile_size-2)

    image = [[] for i in range(image_size)]
    for i, image_array_line in enumerate(image_array):
        for tile_id in image_array_line:
            for j, line in enumerate(tiles[tile_id][DATA][1:-1]):
                for c in line[1:-1]:
                    image[i*(tile_size-2) + j].append(c)

    return image


def create_monster_pattern():
    monsters = []

    # original monster
    monster1 = MONSTER
    monsters.append(monster1)

    # flip vertical
    monster2 = MONSTER[::-1]
    monsters.append(monster2)

    # flip horizontal
    monster3 = []
    for line in MONSTER:
        monster3.append(line[::-1])
    monsters.append(monster3)

    # flip vertical and horizontal
    monster4 = monster3[::-1]
    monsters.append(monster4)

    # rotate clockwise and flip horizontal
    monster5 = [[] for i in range(len(MONSTER[0]))]
    for i, line in enumerate(MONSTER):
        for j, c in enumerate(line):
            monster5[j].append(c)
    monsters.append(monster5)

    # rotate counterclockwise
    monster6 = monster5[::-1]
    monsters.append(monster6)

    # rotate clockwise
    monster7 = []
    for line in monster5:
        monster7.append(line[::-1])
    monsters.append(monster7)

    # rotate clockwise, flip vertical
    monster8 = monster7[::-1]
    monsters.append(monster8)

    return monsters


def show_image(image):
    for line in image:
        print(''.join(line))

    return


def show_monsters(monsters):
    for i, monster in enumerate(monsters):
        print("monster {}:".format(i+1))
        for line in monster:
            print(''.join(line))
        print("")

    return


def solve(image, monsters):
    image_width = len(image[0])
    image_heigh = len(image)
    for monster in monsters:
        monster_width = len(monster[0])
        monster_height = len(monster)

        for y in range(image_heigh-monster_height):
            for x in range(image_width-monster_width):
                exist_monster = True
                for mon_y in range(monster_height):
                    for mon_x in range(monster_width):
                        if monster[mon_y][mon_x] != '#':
                            continue

                        if image[y+mon_y][x+mon_x] == '#' or image[y+mon_y][x+mon_x] == '*':
                            pass
                        else:
                            exist_monster = False
                        if not exist_monster:
                            break
                    if not exist_monster:
                        break
                if exist_monster:
                    for mon_y in range(monster_height):
                        for mon_x in range(monster_width):
                            if monster[mon_y][mon_x] != '#':
                                continue
                            if image[y+mon_y][x+mon_x] == '#':
                                image[y+mon_y][x+mon_x] = '*'

    output = 0
    for y in range(image_heigh):
        for x in range(image_width):
            if image[y][x] == '#':
                output += 1

    return output


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        blocks = f.read().split("\n\n")
        tiles = {}
        for block in blocks:
            lines = block.splitlines()
            if len(lines) == 0:
                break
            id_ = int(lines[0].strip('Title :'))
            # tiles = {
            #     id_: {
            #         "data": [line1_str, line2_str, ...],
            #         "right": None,
            #         "top": None,
            #         "left": None,
            #         "bottom": None,
            #     }
            # }
            tiles[id_] = {DATA: lines[1:], RIGHT: None,
                          TOP: None, LEFT: None, BOTTOM: None}

    image = restore_image(tiles)
    show_image(image)
    monsters = create_monster_pattern()
    show_monsters(monsters)
    output = solve(image, monsters)

    print(output)
