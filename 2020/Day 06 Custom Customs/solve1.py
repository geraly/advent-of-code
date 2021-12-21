def check_answer(answer):
    answer_set = set()

    for c in answer:
        if 'a' <= c and c <= 'z':
            answer_set.add(c)

    return len(answer_set)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    group_answers = data.split("\n\n")

    output = 0
    for answer in group_answers:
        output += check_answer(answer)

    print(output)
