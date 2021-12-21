from enum import Enum, auto


class Color(Enum):
    WHITE = auto()
    BLACK = auto()


class Tile():
    __side = None
    __e = None
    __se = None
    __sw = None
    __w = None
    __nw = None
    __ne = None

    def __init__(self, color: Color):
        self.__side = color

    def flip(self):
        if self.__side == Color.WHITE:
            self.__side = Color.BLACK
        else:
            self.__side = Color.WHITE

    def set_east_tile(self, tile):
        self.__e = tile
        if tile.get_west_tile() != self:
            tile.set_west_tile(self)

    def set_south_east_tile(self, tile):
        self.__se = tile
        if tile.get_north_west_tile() != self:
            tile.set_north_west_tile(self)

    def set_south_west_tile(self, tile):
        self.__sw = tile
        if tile.get_north_east_tile() != self:
            tile.set_north_east_tile(self)

    def set_west_tile(self, tile):
        self.__w = tile
        if tile.get_east_tile() != self:
            tile.set_east_tile(self)

    def set_north_west_tile(self, tile):
        self.__nw = tile
        if tile.get_south_east_tile() != self:
            tile.set_south_east_tile(self)

    def set_north_east_tile(self, tile):
        self.__ne = tile
        if tile.get_south_west_tile() != self:
            tile.set_south_west_tile(self)

    def get_east_tile(self):
        return self.__e

    def get_south_east_tile(self):
        return self.__se

    def get_south_west_tile(self):
        return self.__sw

    def get_west_tile(self):
        return self.__w

    def get_north_west_tile(self):
        return self.__nw

    def get_north_east_tile(self):
        return self.__ne

    def get_side(self):
        return self.__side


class TileFloor():
    __reference_tile: Tile = None
    __tiles: list[list[Tile]] = None

    def __init__(self, size):
        self.__tiles = [[Tile(Color.WHITE) for _ in range(size)]
                        for _ in range(size)]

        # connect neighbor
        for y in range(size - 1):
            for x in range(size - 1):
                self.__tiles[y][x].set_east_tile(self.__tiles[y][x+1])
            if y % 2 == 0:
                for x in range(size):
                    self.__tiles[y][x].set_south_east_tile(
                        self.__tiles[y+1][x])
                for x in range(1, size):
                    self.__tiles[y][x].set_south_west_tile(
                        self.__tiles[y+1][x-1])
            else:
                for x in range(size - 1):
                    self.__tiles[y][x].set_south_east_tile(
                        self.__tiles[y+1][x])
                for x in range(size):
                    self.__tiles[y][x].set_south_west_tile(
                        self.__tiles[y+1][x-1])

        self.__reference_tile = self.__tiles[size//2][size//2]

    def count_tiles(self, color: Color):
        count: int = 0
        for row in self.__tiles:
            for tile in row:
                if tile.get_side() == color:
                    count += 1
        return count

    def flip_tile(self, steps: list[str]):
        p: Tile = self.__reference_tile

        for step in steps:
            if step == 'e':
                p = p.get_east_tile()
            elif step == 'se':
                p = p.get_south_east_tile()
            elif step == 'sw':
                p = p.get_south_west_tile()
            elif step == 'w':
                p = p.get_west_tile()
            elif step == 'nw':
                p = p.get_north_west_tile()
            elif step == 'ne':
                p = p.get_north_east_tile()
            if p is None:
                raise "step is out of range."

        p.flip()

    def flip_tile_with_rule(self):
        size = len(self.__tiles)

        flip_list = []
        # Noneの例外処理が面倒なので端は外して計算する
        for y in range(1, size - 1):
            for x in range(1, size - 1):
                count_neighbor_black = 0
                tile = self.__tiles[y][x]

                color = tile.get_east_tile().get_side()
                if color == Color.BLACK:
                    count_neighbor_black += 1

                color = tile.get_south_east_tile().get_side()
                if color == Color.BLACK:
                    count_neighbor_black += 1

                color = tile.get_south_west_tile().get_side()
                if color == Color.BLACK:
                    count_neighbor_black += 1

                color = tile.get_west_tile().get_side()
                if color == Color.BLACK:
                    count_neighbor_black += 1

                color = tile.get_north_west_tile().get_side()
                if color == Color.BLACK:
                    count_neighbor_black += 1

                color = tile.get_north_east_tile().get_side()
                if color == Color.BLACK:
                    count_neighbor_black += 1

                color = tile.get_side()
                if color == Color.BLACK:
                    if count_neighbor_black == 0 or count_neighbor_black > 2:
                        flip_list.append({'x': x, 'y': y})
                elif color == Color.WHITE:
                    if count_neighbor_black == 2:
                        flip_list.append({'x': x, 'y': y})
                        if x == 1 or x == size - 2 or y == 1 or y == size - 2:
                            raise "floor is too small"

        for f in flip_list:
            self.__tiles[f['y']][f['x']].flip()

    def show_tiles(self):
        output = []
        for row in self.__tiles:
            output_line = []
            for tile in row:
                color = tile.get_side()
                if color == Color.WHITE:
                    output_line.append('w')
                else:
                    output_line.append('b')
            output.append(output_line)

        for y in range(len(output)):
            line_str = " ".join(output[y])
            if y % 2 == 1:
                line_str = " " + line_str

            print(line_str)
