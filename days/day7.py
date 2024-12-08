import itertools

def operate(left, right, symbol):
    if symbol == '*':
        return left * right
    elif symbol == '+':
        return left + right
    elif symbol =='|':
        return int(str(left)+str(right))

def any_answer(result, parts, operators='+*'):
    res = 0

    each_part = parts.split(' ')
    n_combos = len(each_part) - 1

    combos = list(itertools.product(operators, repeat=n_combos))
    for combo in combos:
        total = int(each_part[0])
        for idx in range(1, len(each_part)):
            total = operate(total, int(each_part[idx]), combo[idx-1])

        if total == result:
            res = total
            break

    return res

def part1(input):
    count = 0

    for line in input:
        res = line[0]
        parts = line[1].strip()
        count += any_answer(int(res), parts)

    return count

def part2(input):
    count = 0

    for line in input:
        res = line[0]
        parts = line[1].strip()
        count += any_answer(int(res), parts, '+*|')

    return count

def run(file_name):
    input = []
    with open(file_name, 'r') as file:
        for line in file:
            input.append(line.replace('\n', '').split(':'))

    result1 = part1(input)
    result2 = part2(input)
    print(f"Day 7 - Part 1: {result1}")
    print(f"Day 7 - Part 2: {result2}")