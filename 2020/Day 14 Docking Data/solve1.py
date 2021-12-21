import re


def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    memory = {}
    for line in lines:
        key, val = line.split("=", 1)
        key = key.strip()
        val = val.strip()

        if key == "mask":
            and_mask = 0
            or_mask = 0
            for b in val:
                and_mask <<= 1
                or_mask <<= 1
                if b == '0':
                    # and_mask += 0
                    # or_mask += 0
                    pass
                elif b == '1':
                    and_mask += 1
                    or_mask += 1
                elif b == 'X':
                    and_mask += 1
                    or_mask += 0
                else:
                    print("Format Error")
                    quit()
        else:
            m = re.match(r"mem\[(\d+)\]", key)
            if m is None:
                print("Format Error")
                quit()
            memory[m.group(1)] = int(val) & and_mask | or_mask

    return memory


if __name__ == '__main__':
    memory = read_data("input.txt")

    output = 0
    for val in memory.values():
        output += val

    print(output)
