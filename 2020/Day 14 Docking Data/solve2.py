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
            masks = [{"and_mask": 0, "or_mask": 0}]
            for b in val:
                for mask in masks:
                    mask["and_mask"] <<= 1
                    mask["or_mask"] <<= 1
                if b == '0':
                    for mask in masks:
                        mask["and_mask"] += 1
                        mask["or_mask"] += 0
                elif b == '1':
                    for mask in masks:
                        mask["and_mask"] += 1
                        mask["or_mask"] += 1
                elif b == 'X':
                    masks2 = []
                    for mask in masks:
                        # mask["and_mask"] += 0
                        # mask["or_mask"] += 0
                        masks2.append(
                            {"and_mask": mask["and_mask"] + 1, "or_mask": mask["or_mask"] + 1})
                    masks.extend(masks2)
                else:
                    print("Format Error")
                    quit()
        else:
            m = re.match(r"mem\[(\d+)\]", key)
            if m is None:
                print("Format Error")
                quit()
            address = int(m.group(1))
            for mask in masks:
                masked_address = address & mask["and_mask"] | mask["or_mask"]
                memory[masked_address] = int(val)

    return memory


if __name__ == '__main__':
    memory = read_data("input.txt")

    output = 0
    for val in memory.values():
        output += val

    print(output)
