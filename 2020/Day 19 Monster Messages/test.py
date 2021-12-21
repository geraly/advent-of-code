import unittest
from solve1 import is_valid


class TestIsValid(unittest.TestCase):
    def test_is_valid1(self):
        rule = {
            0: [[4]],
            1: [[2, 3], [3, 2]],
            2: [[4, 4], [5, 5]],
            3: [[4, 5], [5, 4]],
            4: [['a']],
            5: [['b']]
        }
        message = "a"
        self.assertTrue(is_valid(rule, message, 0))

    def test_is_valid2(self):
        rule = {
            0: [[4]],
            1: [[2, 3], [3, 2]],
            2: [[4, 4], [5, 5]],
            3: [[4, 5], [5, 4]],
            4: [['a']],
            5: [['b']]
        }
        message = "b"
        self.assertFalse(is_valid(rule, message, 0))

    def test_is_valid3(self):
        rule = {
            0: [[4]],
            1: [[2, 3], [3, 2]],
            2: [[4, 4], [5, 5]],
            3: [[4, 5], [5, 4]],
            4: [['a']],
            5: [['b']]
        }
        message = "aa"
        self.assertFalse(is_valid(rule, message, 0))

    def test_is_valid4(self):
        rule = {
            0: [[4, 5]],
            1: [[2, 3], [3, 2]],
            2: [[4, 4], [5, 5]],
            3: [[4, 5], [5, 4]],
            4: [['a']],
            5: [['b']]
        }
        message = "ab"
        self.assertTrue(is_valid(rule, message, 0))

    def test_is_valid5(self):
        rule = {
            0: [[4, 5]],
            1: [[2, 3], [3, 2]],
            2: [[4, 4], [5, 5]],
            3: [[4, 5], [5, 4]],
            4: [['a']],
            5: [['b']]
        }
        message = "abb"
        self.assertFalse(is_valid(rule, message, 0))

    def test_is_valid6(self):
        rule = {
            0: [[4, 5]],
            1: [[2, 3], [3, 2]],
            2: [[4, 4], [5, 5]],
            3: [[4, 5], [5, 4]],
            4: [['a']],
            5: [['b']]
        }
        message = "a"
        self.assertFalse(is_valid(rule, message, 0))


if __name__ == "__main__":
    unittest.main()
