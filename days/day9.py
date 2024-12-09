from utils.structs import FileStorage as FS

NO_VALUE = -1

def initial_placement(instructions):
    output = []
    for idx, instruction in enumerate(instructions):
        for i in range(0, instruction.length):
            output.append(instruction.id)
        for i in range(0, instruction.freespace):
            output.append(NO_VALUE)
        
    return output

def move_instruction(instruction, output):
    n_inserted = 0
    output = [x if x != instruction.id else NO_VALUE for x in output]
    for idx in range(0, len(output)):
        if output[idx] == NO_VALUE:
            output[idx] = instruction.id
            n_inserted += 1
        if n_inserted == instruction.length:
            break

    return output


def part1(input):
    total = 0

    input_list = list(input)

    instructions = []
    id = 0
    for idx in range(0, len(input)-1, 2):
        f = FS(id, int(input_list[idx]), int(input_list[idx+1]))
        id += 1
        instructions.append(f)
    
    instructions.append(FS(id, int(input_list[-1]), 0))
    
    output = initial_placement(instructions)
    instructions = instructions[1:]

    for instruction in reversed(instructions):
        output = move_instruction(instruction, output)

    # print(instructions)
    # print(output)

    for idx, out in enumerate(output):
        if out != NO_VALUE:
            total += (idx * out)

    return total

def part2(input):
    return 0

def run(file_name):
    with open(file_name, 'r') as file:
        input = file.read().replace('\n', '')

    result1 = part1(input)
    result2 = part2(input)
    print(f"Day 9 - Part 1: {result1}")
    print(f"Day 9 - Part 2: {result2}")
