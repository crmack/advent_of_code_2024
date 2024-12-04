import re

REG_EX_P1 = r"mul[(]\d{1,3}[,]\d{1,3}[)]"
REG_EX_NUMBERS = r"\d{1,3}"
REG_EX_P2 = r"don[']t[(][)].*?(do[(][)]|$)"

def part1(input):
    total = 0
    cleaned_input = re.findall(REG_EX_P1, input)
    for calc in cleaned_input:
        nums = re.findall(REG_EX_NUMBERS, calc)
        total += int(nums[0]) * int(nums[1])

    return total

def part2(input):
    only_dos = re.sub(REG_EX_P2, "", input)
    return part1(only_dos)

def run(file_name):
    with open(file_name, 'r') as file:
        input = file.read().replace('\n', ' ')

    result1 = part1(input)
    result2 = part2(input)
    print(f"Day 2 - Part 1: {result1}")
    print(f"Day 2 - Part 2: {result2}")
    