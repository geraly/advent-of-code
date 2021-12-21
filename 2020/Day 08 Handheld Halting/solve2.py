import re


def check_terminate_normaly(program):
    executed = []
    accumulator = 0
    eip = 0

    while eip not in executed:
        if eip == len(program):
            return True, accumulator
        elif eip < 0 or len(program) < eip:
            return False, accumulator
        executed.append(eip)
        instruction = program[eip]
        if instruction[0] == "nop":
            eip += 1
        elif instruction[0] == "acc":
            accumulator += instruction[1]
            eip += 1
        elif instruction[0] == "jmp":
            eip += instruction[1]

    return False, accumulator


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

    answer = 0
    for i, code in enumerate(program):
        if code[0] == 'nop':
            program[i] = ('jmp', code[1])
            (isNormal, accumulator) = check_terminate_normaly(program)
            if isNormal:
                answer = accumulator
                break
            program[i] = code
        elif code[0] == 'jmp':
            program[i] = ('nop', code[1])
            (isNormal, accumulator) = check_terminate_normaly(program)
            if isNormal:
                answer = accumulator
                break
            program[i] = code

    print(accumulator)
