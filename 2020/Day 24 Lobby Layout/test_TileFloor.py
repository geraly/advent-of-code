import unittest
import TileFloor


class TestTileFloor(unittest.TestCase):
    def test_functions(self):
        tile_floor = TileFloor.TileFloor(10)
        count = tile_floor.count_tiles(TileFloor.Color.WHITE)
        self.assertEqual(count, 10*10)

        count = tile_floor.count_tiles(TileFloor.Color.BLACK)
        self.assertEqual(count, 0)

        tile_floor.flip_tile(['se'])
        count = tile_floor.count_tiles(TileFloor.Color.WHITE)
        self.assertEqual(count, 10*10 - 1)

    def test_flip_tile_with_rule(self):
        tile_floor = TileFloor.TileFloor(10)
        tile_floor.flip_tile(['se'])
        tile_floor.flip_tile(['sw'])
        count = tile_floor.count_tiles(TileFloor.Color.BLACK)
        self.assertEqual(count, 2)

        tile_floor.flip_tile_with_rule()
        count = tile_floor.count_tiles(TileFloor.Color.BLACK)
        self.assertEqual(count, 4)

    def test_show_tiles(self):
        tile_floor = TileFloor.TileFloor(5)

        print('begin: show_tiles 1')
        tile_floor.show_tiles()

        print('begin: show_tiles 2')
        tile_floor.flip_tile(['se'])
        tile_floor.flip_tile(['sw'])
        tile_floor.show_tiles()

        print('end: show_tiles')

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
