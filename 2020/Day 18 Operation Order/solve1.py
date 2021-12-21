

# )を探す。
# )から数えて一番近い手前の(を探す
#   この範囲内に()はないので、最初から計算していく
# 書き換える
# ()がなくなれば最初から計算していく

def calculate(expr):

    close_index = expr.find(')')
    if close_index >= 0:
        open_index = expr[:close_index].rfind('(')
        ret = calculate(expr[open_index+1:close_index])
        new_expr = expr[:open_index] + \
            str(ret) + expr[close_index+1:]
        return calculate(new_expr)

    terms = expr.split(' ')
    ret = terms.pop(0)
    operator = terms.pop(0)
    for term in terms:
        if term == '+' or term == '*':
            operator = term
        else:  # number
            ret = eval(str(ret) + operator + term)

    return ret


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        expressions = f.read().splitlines()

    output = 0
    for expr in expressions:
        ret = calculate(expr)
        output += ret
        print("{} = {}".format(expr, ret))
    print(output)
