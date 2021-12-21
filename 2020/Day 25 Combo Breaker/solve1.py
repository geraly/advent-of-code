class RoomKey():
    __DIV_NUM = 20201227
    __pub_key = None
    __subject_num = None
    __loop_size = None

    def __init__(self, subject_num, pub_key):
        self.__subject_num = subject_num
        self.__pub_key = pub_key

    def find_loop_count(self):
        loop_size = 1
        v = 1
        while True:
            v = (v * self.__subject_num) % self.__DIV_NUM
            if v == self.__pub_key:
                break
            loop_size += 1
        self.__loop_size = loop_size

    def create_encryption_key(self, pub_key):
        v = 1
        for _ in range(self.__loop_size):
            v = (v * pub_key) % self.__DIV_NUM

        return v


def load_input(filename):
    with open(filename, 'r') as f:
        pub_key1, pub_key2 = f.read().splitlines()

    return int(pub_key1), int(pub_key2)


if __name__ == '__main__':
    card_pub_key, door_pub_key = load_input('input.txt')

    card_key = RoomKey(7, card_pub_key)
    card_key.find_loop_count()
    encryption_key = card_key.create_encryption_key(door_pub_key)
    print(encryption_key)
