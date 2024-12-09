from utils.structs import FileStorage as FS

NO_VALUE = -1

def initial_placement(instructions):
    output = []
    for instruction in instructions:
        for _ in range(0, instruction.length):
            output.append(instruction.id)
        for _ in range(0, instruction.freespace):
            output.append(NO_VALUE)
        
    return output

def move_instruction(instruction, output):
    # Make sure we need to even check this
    first_empty = output.index(NO_VALUE)
    ins_start = output.index(instruction.id)
    if ins_start <= first_empty:
        return output
    
    # Zero out the old positions (if it ends up overlapping back into its same spot; fine)
    output = [x if x != instruction.id else NO_VALUE for x in output]

    # Do the moving
    n_inserted = 0
    for idx in range(0, len(output)):
        if output[idx] == NO_VALUE:
            output[idx] = instruction.id
            n_inserted += 1
        if n_inserted == instruction.length:
            break

    return output

def move_full_instruction(instruction, output):
    n_needed = instruction.length
    original_indices = [i for i, x in enumerate(output) if x == instruction.id]

    start_idx = original_indices[0]
    # Don't bother if there are no empty spaces to the left of the current instruction
    first_empty = output.index(NO_VALUE)
    if start_idx <= first_empty:
        return output

    did_move = False
    # check if there is enough room in any empty space
    for idx in range(0, start_idx):
        n_found = 0
        s = idx
        while s < len(output) and output[s] == NO_VALUE:
            n_found += 1
            s += 1
        
        if n_found >= n_needed:
            for i in range(idx, idx+n_needed):
                output[i] = instruction.id

            did_move = True
            break


    if did_move:
        for idx in original_indices:
            output[idx] = NO_VALUE

    return output


def part1(input, move_whole=False):
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
        if move_whole:
            output = move_full_instruction(instruction, output)
        else:
            output = move_instruction(instruction, output)

    for idx, out in enumerate(output):
        if out != NO_VALUE:
            total += (idx * out)

    return total

def part2(input):
    return part1(input, True)

def run(file_name):
    with open(file_name, 'r') as file:
        input = file.read().replace('\n', '')

    result1 = part1(input)
    print(f"Day 9 - Part 1: {result1}")
    result2 = part2(input)
    print(f"Day 9 - Part 2: {result2}")
