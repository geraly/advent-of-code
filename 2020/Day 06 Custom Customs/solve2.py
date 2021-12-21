def check_answer(answer):

    lines = answer.splitlines()
    answer_set = set(lines.pop())

    for line in lines:
        work_set = set(line)
        answer_set &= work_set

    return len(answer_set)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    group_answers = data.split("\n\n")

    output = 0
    for answer in group_answers:
        output += check_answer(answer)

    print(output)
