import re


def remove_invalid_ticket(rule, nearby_ticket):
    invalid_tickets = []
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
                invalid_tickets.append(ticket)
                break

    for ticket in invalid_tickets:
        nearby_ticket.remove(ticket)

    return


def determine_field(rule, nearby_ticket):
    # field_index_candidate = {
    #   "class": [1, 2],
    #   "row": [0, 1, 2],
    #   "seat": [2]
    # }
    field_index_candidate = {}
    field_num = len(nearby_ticket[0])

    # search possible field
    for field, ranges in rule.items():
        field_index_candidate[field] = set()
        for i in range(field_num):
            is_valid = True
            for ticket in nearby_ticket:
                if ranges[0][0] <= ticket[i] and ticket[i] <= ranges[0][1]:
                    pass
                elif ranges[1][0] <= ticket[i] and ticket[i] <= ranges[1][1]:
                    pass
                else:
                    is_valid = False
                    break
            if is_valid:
                field_index_candidate[field].add(i)

    # field_index = {
    #   "class": 1,
    #   "row": 0,
    #   "seat": 2
    # }
    field_index = {}

    # determine field
    while True:
        remove_field = None
        for k, v in field_index_candidate.items():
            if len(v) == 1:
                remove_field = k
                remove_field_index = v.pop()
                field_index[k] = remove_field_index
                break
        if remove_field is None:
            break
        field_index_candidate.pop(remove_field)
        for k in field_index_candidate.keys():
            field_index_candidate[k].remove(remove_field_index)

    if len(field_index) != field_num:
        print("Needs further search")
        return field_index

    return field_index


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

    remove_invalid_ticket(rule, nearby_ticket)
    field_index = determine_field(rule, nearby_ticket)

    output = 1
    for field, index in field_index.items():
        if field.startswith("departure"):
            output *= your_ticket[index]
    print(output)
