def calculate(expr):
    close_index = expr.find(')')
    if close_index >= 0:
        open_index = expr[:close_index].rfind('(')
        ret = calculate(expr[open_index+1:close_index])
        new_expr = expr[:open_index] + \
            str(ret) + expr[close_index+1:]
        return calculate(new_expr)

    terms = expr.split(' ')

    while len(terms) > 1:
        try:
            plus_index = terms.index('+')
            num = eval(''.join(terms[plus_index-1:plus_index+2]))
            terms = terms[:plus_index-1] + terms[plus_index+1:]
            terms[plus_index-1] = str(num)
        except ValueError:
            break

    while len(terms) > 1:
        num = eval(''.join(terms[0:3]))
        terms = terms[2:]
        terms[0] = str(num)

    return int(terms[0])


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        expressions = f.read().splitlines()

    output = 0
    for expr in expressions:
        ret = calculate(expr)
        output += ret
        print("{} = {}".format(expr, ret))
    print(output)
