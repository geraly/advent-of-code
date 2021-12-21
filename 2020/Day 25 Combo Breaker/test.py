import unittest
import solve1


class TestSolve1(unittest.TestCase):
    def test_load_input(self):
        card_pub_key, door_pub_key = solve1.load_input('example.txt')

        card_key = solve1.RoomKey(7, card_pub_key)
        card_key.find_loop_count()
        encryption_key = card_key.create_encryption_key(door_pub_key)
        self.assertEqual(encryption_key, 14897079)


if __name__ == '__main__':
    unittest.main()
