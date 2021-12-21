import re


if __name__ == '__main__':

    # a contains b, c
    # c contains z
    # rule = {"b": ["a"], "c": ["a"], "z": ["c"]}

    rule = {}
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            m = re.match(r'(.+) bags contain (.+)', line)
            if m is None:
                raise Exception("format error")
            subject = m.group(1)
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
                bag = m2.group(2)
                if bag in rule:
                    rule[bag].add(subject)
                else:
                    rule[bag] = set([subject])
    answer = set()
    queue = []

    for bag in rule["shiny gold"]:
        answer.add(bag)
        queue.append(bag)

    while len(queue) > 0:
        bag = queue.pop()
        if bag not in rule:
            continue
        for b in rule[bag]:
            if b not in answer:
                answer.add(b)
                queue.append(b)

    print(len(answer))
