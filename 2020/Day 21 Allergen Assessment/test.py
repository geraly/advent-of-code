import unittest
import solve1


class TestSolve1(unittest.TestCase):
    def test_count_ingredient(self):
        list_ = [
            {'allergen': ['dairy', 'fish'],
             'ingredient': ['mxmxvkd', 'kfcds', 'sqjhc', 'nhms']},
            {'allergen': ['dairy'],
             'ingredient': ['trh', 'fvjkl', 'sbzzf', 'mxmxvkd']},
            {'allergen': ['soy'],
             'ingredient': ['sqjhc', 'fvjkl']},
            {'allergen': ['fish'],
             'ingredient': ['sqjhc', 'mxmxvkd', 'sbzzf']}
        ]

        ingredient = ['kfcds', 'nhms', 'sbzzf', 'trh']

        self.assertEqual(solve1.count_ingredient(list_, ingredient), 5)


if __name__ == "__main__":
    unittest.main()
