
def get_edges(tile):
    #   1
    # 2   0
    #   3
    edge0 = []
    edge2 = []
    for i in range(len(tile)):
        edge0.append(tile[i][len(tile)-1])
        edge2.append(tile[i][0])

    return ''.join(edge0), tile[0], ''.join(edge2), tile[-1]


def is_neighbor(tile1, tile2):
    edges1 = get_edges(tile1)
    edges2 = get_edges(tile2)

    for edge1 in edges1:
        for edge2 in edges2:
            if edge1 == edge2 or edge1 == edge2[::-1]:
                return True

    return False


def search_corner_tile(tiles):

    corner_tiles = []
    for id1, tile1 in tiles.items():
        neighbor_count = 0
        for id2, tile2 in tiles.items():
            if id1 == id2:
                continue
            if is_neighbor(tile1, tile2):
                neighbor_count += 1
            if neighbor_count == 4:
                break
        if neighbor_count == 2:
            corner_tiles.append(id1)
            if len(corner_tiles) == 4:
                break

    return corner_tiles


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        blocks = f.read().split("\n\n")
        tiles = {}
        for block in blocks:
            lines = block.splitlines()
            if len(lines) == 0:
                break
            id_ = int(lines[0].strip('Title :'))
            tiles[id_] = lines[1:]

    output = 1
    for id_ in search_corner_tile(tiles):
        output *= id_
    print(output)
