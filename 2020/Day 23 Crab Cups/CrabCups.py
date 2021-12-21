class CrabCup():
    __label = None
    __next = None
    __prev = None

    def __init__(self, label):
        self.__label = label

    def set_label(self, label):
        self.__label = label

    def set_next_cup(self, cup):
        self.__next = cup
        if cup.get_prev_cup() != self:
            cup.set_prev_cup(self)

    def set_prev_cup(self, cup):
        self.__prev = cup
        if cup.get_next_cup() != self:
            cup.set_next_cup(self)

    def get_label(self):
        return self.__label

    def get_next_cup(self):
        return self.__next

    def get_prev_cup(self):
        return self.__prev


class CrabCups():
    __PICK_UP_SIZE = 3
    __size = 0
    __current_cup = None
    __table = None

    def __init__(self, labels):
        cups = [CrabCup(label) for label in labels]

        # self.__table[0] is never used
        self.__table = [None] * (len(cups)+1)
        for cup in cups:
            self.__table[cup.get_label()] = cup

        for i in range(len(cups)-1):
            cups[i].set_next_cup(cups[i+1])
        cups[-1].set_next_cup(cups[0])

        self.__current_cup = cups[0]
        self.__size = len(cups)

    def move(self):
        # pick up cup
        next_cup = first_pic_up_cup = self.__current_cup.get_next_cup()
        for _ in range(self.__PICK_UP_SIZE):
            next_cup = next_cup.get_next_cup()
        last_pic_up_cup = next_cup.get_prev_cup()
        self.__current_cup.set_next_cup(next_cup)

        # search destination
        destination_label = self.__current_cup.get_label() - 1
        if destination_label <= 0:
            destination_label = self.__size
        # 現在のカップのラベルの値-1がpick upしたカップに含まれているかを探す
        pick_up_labels = []
        p = first_pic_up_cup
        while True:
            pick_up_labels.append(p.get_label())
            if p == last_pic_up_cup:
                break
            p = p.get_next_cup()
        while destination_label in pick_up_labels:
            destination_label -= 1
            if destination_label <= 0:
                destination_label = self.__size
        destination_cup = self.__table[destination_label]

        # place the cups
        destination_cup.get_next_cup().set_prev_cup(last_pic_up_cup)
        destination_cup.set_next_cup(first_pic_up_cup)

        self.__current_cup = self.__current_cup.get_next_cup()

    def get_labels(self, shift_pos=0):
        output = []
        shift_pos = shift_pos % self.__size

        start_cup = self.__current_cup
        for _ in range(shift_pos):
            start_cup = start_cup.get_prev_cup()
        cup = start_cup
        for _ in range(self.__size):
            output.append(cup.get_label())
            cup = cup.get_next_cup()

        return output

    def find_cup(self, label):
        cup = self.__current_cup
        for _ in range(self.__size):
            if cup.get_label() == label:
                return cup
            cup = cup.get_next_cup()

        return None

    def get_answer1(self):
        output = []
        cup = self.find_cup(1).get_next_cup()
        for _ in range(self.__size - 1):
            output.append(cup.get_label())
            cup = cup.get_next_cup()

        return "".join(list(map(str, output)))

    def get_answer2(self):
        cup1 = self.__table[1].get_next_cup()
        cup2 = cup1.get_next_cup()

        return cup1.get_label(), cup2.get_label()
