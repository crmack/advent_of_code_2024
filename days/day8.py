import math

from utils.funcs import valid_pos

def antinode_positions(antenna1, antenna2, sx, sy, keep_going=False):
    ret = []

    # "keep_going" means antinodes will exist on all of the antennas regardless of how the rest shakes out
    if keep_going:
        ret.append(f"{antenna1[0]},{antenna1[1]}")
        ret.append(f"{antenna2[0]},{antenna2[1]}")

    dx = antenna1[1] - antenna2[1]
    dy = antenna1[0] - antenna2[0]

    nx1 = antenna1[1]+dx
    ny1 = antenna1[0]+dy
    nx2 = antenna2[1]-dx
    ny2 = antenna2[0]-dy

    if valid_pos(nx1, ny1, sx, sy):
        ret.append(f"{ny1},{nx1}")
        if keep_going:
            # Keep going out until you cross a boundary
            valid = True
            while valid:
                nx1 += dx
                ny1 += dy
                valid = valid_pos(nx1, ny1, sx, sy)
                if valid:
                    ret.append(f"{ny1},{nx1}")

    
    if valid_pos(nx2, ny2, sx, sy):
        ret.append(f"{antenna2[0]-dy},{antenna2[1]-dx}")
        if keep_going:
            # Keep going out until you cross a boundary
            valid = True
            while valid:
                nx2 -= dx
                ny2 -= dy
                valid = valid_pos(nx2, ny2, sx, sy)
                if valid:
                    ret.append(f"{ny2},{nx2}")

    return ret


def place_antinodes(grid, antenna, keep_going=False):
    antinodes = {}
    sx = len(grid[0])
    sy = len(grid)

    # Find the locations of the instances of the current antenna in the grid
    full_grid_str = "".join(grid)
    locs = [pos for pos, char in enumerate(full_grid_str) if char == antenna]
    
    # Compare each antenna with each other antenna
    for big_idx in range(0, len(locs)):
        y1 = int(math.floor(locs[big_idx] / len(grid[0])))
        x1 = int(locs[big_idx] % len(grid[0]))
        for idx in range(big_idx+1, len(locs)):
            y2 = int(math.floor(locs[idx] / len(grid[0])))
            x2 = int(locs[idx] % len(grid[0]))
            positions = antinode_positions([y1, x1], [y2, x2], sx, sy, keep_going)
            for pos in positions:
                if pos in antinodes:
                    antinodes[pos] += 1
                else:
                    antinodes[pos] = 1

    return antinodes

def part1(input, keep_going=False):
    antinode_dict = {}

    # Find all of the unique characters in the input
    unique = set("".join(set(input)))
    # Remove the empty locations ('.')
    unique.remove('.')
    
    for symbol in unique:
        positions = place_antinodes(input, symbol, keep_going)
        for pos, count in positions.items():
            if pos in antinode_dict:
                antinode_dict[pos] += count
            else:
                antinode_dict[pos] = count

    return len(antinode_dict)

def part2(input):
    return part1(input, True)

def run(file_name):
    input = []
    with open(file_name, 'r') as file:
        for line in file:
            input.append(line.replace('\n', ''))

    result1 = part1(input)
    result2 = part2(input)
    print(f"Day 8 - Part 1: {result1}")
    print(f"Day 8 - Part 2: {result2}")
