import re
from utils.coords import Point2D

FIND_X_RE = r"X"
FIND_M_RE = r"M"

DIRECTIONS = [Point2D(-1,-1), Point2D(0,-1), Point2D(1,-1), Point2D(-1,0), Point2D(1,0), Point2D(-1,1), Point2D(0,1), Point2D(1,1)]
DIRECTIONS_P2 = [Point2D(-1,-1), Point2D(1,-1), Point2D(-1,1), Point2D(1,1)]

def letter_match(all_data, coord, next_letter, direction):
    new_x = coord.x + direction.x
    if new_x < 0 or new_x >= len(all_data[0]):
        return 0
    
    new_y = coord.y + direction.y
    if new_y < 0 or new_y >= len(all_data):
        return 0
    
    if all_data[new_y][new_x] == next_letter:
        return 1
    
    return 0

def find_next_letter(all_data, coord, word, letter_idx, direction):
    if letter_match(all_data,coord,word[letter_idx],direction):
        if letter_idx == len(word) - 1:
            return (1, direction)
        return find_next_letter(all_data, Point2D(coord.x+direction.x,coord.y+direction.y), word, letter_idx+1, direction)
        
    return (0, None)


def find_word(all_data, start_letter_coords, word_to_find, directions=DIRECTIONS):
    count = 0
    dirs = []
    for d in directions:
        (c, dir) = find_next_letter(all_data, start_letter_coords, word_to_find, 1, d)
        count += c
        if dir:
            dirs.append(dir)

    return (count, dirs)

def part1(input):
    count = 0
    for y, row in enumerate(input):
        xs = re.finditer(FIND_X_RE, row)
        for match in xs:
            (c, _) = find_word(input, Point2D(match.start(0), y), "XMAS")
            count += c

    return count

def part2(input):
    count = 0
    all_as = {}

    # Find all Ms so you can find all MAS, saving coordinates of the As in each...then accept any with duplicate As
    for y, row in enumerate(input):
        xs = re.finditer(FIND_M_RE, row)
        for match in xs:
            (_, dirs) = find_word(input, Point2D(match.start(0), y), "MAS", DIRECTIONS_P2)
            for d in dirs:
                a_loc = str([match.start(0) + d.x, y + d.y])
                if a_loc in all_as:
                    all_as[a_loc] += 1
                else:
                    all_as[a_loc] = 1

    for k,v in all_as.items():
        if v > 1:
            count += 1
            
    return count


def run(file_name):
    rows = []
    with open(file_name, 'r') as file:
        for line in file:
            rows.append(line.replace('\n', ''))

    result1 = part1(rows)
    result2 = part2(rows)
    print(f"Day 4 - Part 1: {result1}")
    print(f"Day 4 - Part 2: {result2}")
    