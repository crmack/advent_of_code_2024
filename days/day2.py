MAX_DIFF = 3

def is_valid(row):
    if sorted(row) != row and sorted(row, reverse=True) != row:
        return 0
    
    diffs = [row[n]-row[n-1] for n in range(1,len(row))]
    if max(diffs) > MAX_DIFF or min(diffs) < -MAX_DIFF or diffs.count(0):
        return 0
    
    return 1


def is_valid_forgiveness(row):
    if is_valid(row):
        return 1
    
    for n in range(0, len(row)):
        new_row = [e for i, e in enumerate(row) if i != n]
        if is_valid(new_row):
            return 1
        
    return 0


def part1(rows):
    valid = []
    for r in rows:
        valid.append(is_valid(r))

    return sum(valid)


def part2(rows):
    valid = []
    for r in rows:
        valid.append(is_valid_forgiveness(r))

    return sum(valid)


def run(file_name):
    f = open(file_name, "r")
    rows = []
    for line in f:
        rows.append([int(x) for x in line.split(None)])

    f.close()

    total_valid = part1(rows)
    total_valid_p2 = part2(rows)
    print(f"Day 2 - Part 1: {total_valid}")
    print(f"Day 2 - Part 2: {total_valid_p2}")
