import re

from utils.printy import print2dArray
from utils.structs import Point2D as P

RE_NUM = r"\d+"

def solve(a, b, p, p_offset=0):
    # p.x = a.x * A + b.x * B
    # 8400 = 94*A + 22*B
    # p.y = a.y * A + b.y * B
    # 5400 = 34*A + 67*B

    # I remembered enough linear algebra to know there was a solution to this, but had to dig a bit to find it (Cramer's Rule)
    # https://courses.lumenlearning.com/odessa-collegealgebra/chapter/using-cramers-rule-to-solve-a-system-of-two-equations-in-two-variables/

    p.x += p_offset
    p.y += p_offset

    nA = int(((p.x * b.y) - (p.y * b.x)) / ((a.x * b.y) - (a.y * b.x)))
    nB = int(((a.x * p.y) - (a.y * p.x)) / ((a.x * b.y) - (a.y * b.x)))

    if (nA * a.x + nB * b.x == p.x) and (nA * a.y + nB * b.y == p.y):
        return P(nA, nB)

    return P(0,0)

def part1(a, b, p):
    total_a = 0
    total_b = 0

    for idx in range(0, len(a)):
        solved = solve(a[idx], b[idx], p[idx])
        total_a += solved.x
        total_b += solved.y


    return total_a * 3 + total_b

def part2(a, b, p):
    total_a = 0
    total_b = 0

    for idx in range(0, len(a)):
        solved = solve(a[idx], b[idx], p[idx], 10000000000000)
        total_a += solved.x
        total_b += solved.y


    return total_a * 3 + total_b

def parse_line(line):
    nums = re.findall(RE_NUM, line)
    return P(int(nums[0]), int(nums[1]))


def run(file_name):
    a = []
    b = []
    p = []
    with open(file_name, 'r') as file:
        for line in file:
            if 'Button A' in line:
                a.append(parse_line(line))
            elif 'Button B' in line:
                b.append(parse_line(line))
            elif 'Prize' in line:
                p.append(parse_line(line))

    result1 = part1(a, b, p)
    result2 = part2(a, b, p)
    print(f"Day 13 - Part 1: {result1}")
    print(f"Day 13 - Part 2: {result2}")
