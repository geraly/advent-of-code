import unittest
from solve1 import get_edges, is_neighbor
from solve2 import flip_vertical, flip_horizontal, rotate, DATA, LEFT, TOP, RIGHT, BOTTOM


class TestSolve1(unittest.TestCase):
    def test_get_edges1(self):
        tile = [
            "#.#.",
            "#.#.",
            "#.#.",
            "...#",
        ]

        self.assertTupleEqual(
            get_edges(tile), ('...#', '#.#.', '###.', '...#'))

    def test_is_neighbor1(self):
        tile1 = [
            "#.#.",
            "#.#.",
            "#.#.",
            "...#",
        ]

        tile2 = [
            "....",
            "..#.",
            "..#.",
            "....",
        ]

        self.assertFalse(is_neighbor(tile1, tile2))

    def test_is_neighbor2(self):
        tile1 = [
            "#.#.",
            "#.#.",
            "#.#.",
            "...#",
        ]

        tile2 = [
            ".#.#",
            "#.##",
            "#.#.",
            ".##.",
        ]

        self.assertTrue(is_neighbor(tile1, tile2))

    def test_is_neighbor3(self):
        tile1 = [
            "#.#.",
            "#.#.",
            "#.#.",
            "...#",
        ]

        tile2 = [
            ".###",
            "#.#.",
            "..#.",
            "#..#",
        ]

        self.assertTrue(is_neighbor(tile1, tile2))

    def test_is_neighbor4(self):
        tile1 = [
            "#.#.",
            "#.#.",
            "#.#.",
            "...#",
        ]

        tile2 = [
            "####",
            "..#.",
            "#.#.",
            "...#",
        ]

        self.assertTrue(is_neighbor(tile1, tile2))


class TestSolve2(unittest.TestCase):
    def test_flip_vertical(self):
        tile_data = [
            "#.#.",
            "#.#.",
            "#.#.",
            "...#",
        ]
        tile = {DATA: tile_data, RIGHT: 1,
                TOP: 2, LEFT: 3, BOTTOM: 4}

        self.assertEqual(
            flip_vertical(tile), {DATA: ['...#', '#.#.', '#.#.', '#.#.'], RIGHT: 1, TOP: 4, LEFT: 3, BOTTOM: 2})

    def test_flip_horizontal(self):
        tile_data = [
            "#.#.",
            "#.#.",
            "#.#.",
            "...#",
        ]
        tile = {DATA: tile_data, RIGHT: 1,
                TOP: 2, LEFT: 3, BOTTOM: 4}
        self.assertEqual(
            flip_horizontal(tile), {DATA: ['.#.#', '.#.#', '.#.#', '#...'], RIGHT: 3, TOP: 2, LEFT: 1, BOTTOM: 4})

    def test_rotate1(self):
        tile_data = [
            "#.#.",
            "#.#.",
            "#.#.",
            "...#",
        ]
        tile = {DATA: tile_data, RIGHT: 1,
                TOP: 2, LEFT: 3, BOTTOM: 4}
        self.assertEqual(
            rotate(tile), {DATA: ['...#', '###.', '....', '###.'], RIGHT: 2, TOP: 3, LEFT: 4, BOTTOM: 1})

    def test_rotate2(self):
        tile_data = [
            "#.#.",
            "#.#.",
            "#.#.",
            "...#",
        ]
        tile = {DATA: tile_data, RIGHT: 1,
                TOP: 2, LEFT: 3, BOTTOM: 4}

        self.assertEqual(
            rotate(tile, RIGHT), {DATA: ['.###', '....', '.###', '#...'], RIGHT: 4, TOP: 1, LEFT: 2, BOTTOM: 3})


if __name__ == "__main__":
    unittest.main()
