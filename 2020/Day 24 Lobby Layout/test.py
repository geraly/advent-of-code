import unittest
import solve1
import solve2


class TestSolve1(unittest.TestCase):
    def test_load_input(self):
        steps = solve1.load_input('example.txt')
        self.assertEqual(steps[0], ['se', 'se', 'nw', 'ne', 'ne', 'ne', 'w', 'se',
                                    'e', 'sw', 'w', 'sw', 'sw', 'w', 'ne', 'ne', 'w', 'se', 'w', 'sw'])

    def test_solve1(self):
        steps = solve1.load_input('example.txt')
        tile_floor = solve1.TileFloor(100)
        solve1.flip_tiles(tile_floor, steps)
        answer = tile_floor.count_tiles(solve1.Color.BLACK)
        self.assertEqual(answer, 10)


class TestSolve2(unittest.TestCase):
    def test_solve(self):
        steps = solve2.load_input('example.txt')
        tile_floor = solve2.TileFloor(1000)
        solve2.flip_tiles(tile_floor, steps)
        counts = []
        for _ in range(100):
            tile_floor.flip_tile_with_rule()
            counts.append(tile_floor.count_tiles(solve2.Color.BLACK))

        self.assertEqual(counts[0], 15)
        self.assertEqual(counts[1], 12)
        self.assertEqual(counts[2], 25)
        self.assertEqual(counts[3], 14)
        self.assertEqual(counts[4], 23)
        self.assertEqual(counts[5], 28)
        self.assertEqual(counts[6], 41)
        self.assertEqual(counts[7], 37)
        self.assertEqual(counts[8], 49)
        self.assertEqual(counts[9], 37)

        self.assertEqual(counts[19], 132)
        self.assertEqual(counts[29], 259)
        self.assertEqual(counts[39], 406)
        self.assertEqual(counts[49], 566)
        self.assertEqual(counts[59], 788)
        self.assertEqual(counts[69], 1106)
        self.assertEqual(counts[79], 1373)
        self.assertEqual(counts[89], 1844)
        self.assertEqual(counts[99], 2208)


if __name__ == '__main__':
    unittest.main()
