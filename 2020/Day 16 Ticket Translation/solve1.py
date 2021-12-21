import re


def solve(rule, nearby_ticket):
    output = 0
    for ticket in nearby_ticket:
        for field in ticket:
            is_valid = False
            for ranges in rule.values():
                if ranges[0][0] <= field and field <= ranges[0][1]:
                    is_valid = True
                    break
                elif ranges[1][0] <= field and field <= ranges[1][1]:
                    is_valid = True
                    break
            if not is_valid:
                output += field

    return output


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        rule = {}
        your_ticket = []
        nearby_ticket = []
        block = f.read().split("\n\n")

        for line in block[0].splitlines():
            m = re.match(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", line)
            if m is None:
                print("Format Error")
                print(line)
                quit()
            field, min1, max1, min2, max2 = m.groups()
            rule[field] = [(int(min1), int(max1)), (int(min2), int(max2))]

        your_ticket = list(map(int, block[1].split("\n")[1].split(',')))

        for line in block[2].splitlines()[1:]:
            nearby_ticket.append(list(map(int, line.split(','))))

    print(solve(rule, nearby_ticket))
