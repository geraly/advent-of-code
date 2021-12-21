import re


def count_inner_bags(rule, bag):
    return count_all_bags(rule, bag) - 1


def count_all_bags(rule, bag):

    if len(rule[bag]) == 0:
        return 1
    else:
        count = 1
        for inner_bag, inner_bag_num in rule[bag].items():
            count += inner_bag_num * count_all_bags(rule, inner_bag)
        return count


if __name__ == '__main__':

    # a contains 2 b, 3 c
    # c contains z
    # d contains no other bags
    # rule = {"a": {"b":2, "c": 3}, "c": {"z": 1}, "d": {}}

    rule = {}
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            m = re.match(r'(.+) bags contain (.+)', line)
            if m is None:
                raise Exception("format error")
            outer_bag = m.group(1)
            rule[outer_bag] = {}
            # m.group(2)
            # no other bags.
            # 1 mirrored green bag, 5 shiny maroon bags.
            for work in m.group(2).split(','):
                if work.startswith('no other bags.'):
                    continue
                # work
                # 1 mirrored green bag
                #  5 shiny maroon bags.
                m2 = re.match(r'\s*(\d+) (.+) bags*\.*', work)
                if m2 is None:
                    raise Exception("format error")
                inner_bag_num = int(m2.group(1))
                inner_bag = m2.group(2)
                rule[outer_bag][inner_bag] = inner_bag_num

    print(count_inner_bags(rule, "shiny gold"))
