import re


if __name__ == '__main__':

    # program = [("nop", "+0"), ("acc", "+1"), ...]
    program = []
    with open('input.txt', 'r') as f:
        for line in f.read().splitlines():
            m = re.match(r'(.+) (.+)', line)
            if m is None:
                raise Exception("format error")
            opecode = m.group(1)
            operand = int(m.group(2))
            program.append((opecode, operand))

    executed = []
    accumulator = 0
    eip = 0

    while eip not in executed:
        executed.append(eip)
        instruction = program[eip]
        if instruction[0] == "nop":
            eip += 1
        elif instruction[0] == "acc":
            accumulator += instruction[1]
            eip += 1
        elif instruction[0] == "jmp":
            eip += instruction[1]

    print(accumulator)
