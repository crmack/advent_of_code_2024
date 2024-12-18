import re

RE_NUM = r"-?\d+"

def get_combo_operand(operand, registers):
    if operand <= 3:
        return operand
    if operand == 4:
        return registers['A']
    if operand == 5:
        return registers['B']
    if operand == 6:
        return registers['C']

def perform_opcode(registers, opcode, operand, instruction_idx):
    if opcode == 0:
        num = registers['A']
        dom = 2 ** get_combo_operand(operand, registers)
        registers['A'] = int(num/dom)
    elif opcode == 1:
        b = registers['B']
        registers['B'] = b ^ operand
    elif opcode == 2:
        registers['B'] = get_combo_operand(operand, registers) % 8
    elif opcode == 3:
        if registers['A'] != 0:
            return operand, None
    elif opcode == 4:
        registers['B'] = registers['B'] ^ registers['C']
    elif opcode == 5:
        out = str(get_combo_operand(operand, registers) % 8)
        return instruction_idx, out
    elif opcode == 6:
        num = registers['A']
        dom = 2 ** get_combo_operand(operand, registers)
        registers['B'] = int(num/dom)
    elif opcode == 7:
        num = registers['A']
        dom = 2 ** get_combo_operand(operand, registers)
        registers['C'] = int(num/dom)

    return instruction_idx, None


def part1(registers, program):
    idx = 0
    outs = []
    while True:
        if idx >= len(program) - 1:
            break
        new_idx, out = perform_opcode(registers, program[idx], program[idx+1], idx)
        if out:
            outs.append(out)
        if new_idx == idx:
            idx += 2
        else:
            idx = new_idx

    return ",".join(outs)


def run_once(ins):
    a = ins[0]
    registers = {'A': a}
    program = ins[1]
    idx = 0
    outs = []
    go = True
    while go:
        if idx >= len(program) - 1:
            break
        new_idx, out = perform_opcode(registers, program[idx], program[idx+1], idx)
        if new_idx == idx:
            idx += 2
        else:
            idx = new_idx

        if out:
            outs.append(int(out))

    return outs

def part2(program):
    # Work backwards on the expected output.
    # Find all the 3 bit combos (0-7 int) that satisfy that output position
    # Shift those matches to the left by three and repeat for the next output value (working backwards)
    # Repeat until all of the output has been reconstructed
    # This mainly serves to limit the number of times you have to run the program by a bunch of orders of magnitude
    # the "brute" here is limited to a very small number (was < 2000 for my input) instead of 8 ** 16
    good_vals = [0]
    for x, _ in enumerate(reversed(program)):
        possible_results = []
        for i in range(0, 8, 1):
            for v in good_vals:
                a = v << 3
                res = run_once((i+a, program))
                if res is not None:
                    possible_results.append((a+i, res))

        good_vals = []
        for a, res in possible_results:
            if res == program[-(x+1):]:
                good_vals.append(a)

    return min(good_vals)


def run(file_name):
    registers = {}
    program = []

    with open(file_name, 'r') as file:
        for line in file:
            if 'Register A' in line:
                nums = re.findall(RE_NUM, line)
                registers['A'] = int(nums[0])
            elif 'Register B' in line:
                nums = re.findall(RE_NUM, line)
                registers['B'] = int(nums[0])
            elif 'Register C' in line:
                nums = re.findall(RE_NUM, line)
                registers['C'] = int(nums[0])
            elif 'Program' in line:
                nums = re.findall(RE_NUM, line)
                for num in nums:
                    program.append(int(num))

    print(f"Registers: {registers} and program: {program}")

    result1 = part1(registers, program)
    result2 = part2(program)
    print(f"Day 17 - Part 1: {result1}")
    print(f"Day 17 - Part 2: {result2}")
