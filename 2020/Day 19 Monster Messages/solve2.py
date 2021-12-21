import copy
import time


def is_valid(rule, message, rule_no):
    target_rules = copy.copy(rule[rule_no])

    while len(target_rules) > 0:
        one_rule = target_rules.pop(0)
        is_chars_only_rule = True
        for i in range(len(one_rule)):
            if type(one_rule[i]) is str:
                if len(message) <= i or message[i] != one_rule[i]:
                    is_chars_only_rule = False
                    break
            else:
                is_chars_only_rule = False
                next_rules = rule[one_rule[i]]
                for next_rule in next_rules:
                    target_rules.insert(
                        0, one_rule[:i] + next_rule + one_rule[i+1:])
                break
        if is_chars_only_rule:
            one_rule_str = ''.join(one_rule)
            if message == one_rule_str:
                return True

    return False


if __name__ == '__main__':
    with open("input2.txt", "r") as f:
        block = f.read().split("\n\n")
        # rule = {
        #     0: [[4, 1, 5]],
        #     1: [[2, 3], [3, 2]],
        #     2: [[4, 4], [5, 5]],
        #     3: [[4, 5], [5, 4]],
        #     4: [['a']],
        #     5: [['b']]
        # }
        rule = {}
        for line in block[0].splitlines():
            # 1: 2 3 | 3 2
            # 4: "a"
            rule_no, rule_value_str = line.split(':')
            rule_no = int(rule_no)
            if rule_value_str.find('"') >= 0:
                rule_value = [[rule_value_str.strip('" ')]]
            else:
                rule_value = []
                for rule_value_one in rule_value_str.split('|'):
                    rule_value.append(
                        list(map(int, rule_value_one.strip().split(' '))))
            rule[rule_no] = rule_value
        messages = block[1].splitlines()

    output = 0
    start = lap1 = time.time()
    for message in messages:
        lap2 = time.time()
        if is_valid(rule, message, 0):
            output += 1
        print("{}".format(lap2-lap1))
        lap2 = lap1
    end = time.time()
    print("{}".format(end-start))

    print(output)
