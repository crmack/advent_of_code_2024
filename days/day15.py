from utils.printy import print2dArray
from utils.structs import Point2D as P
from utils.structs import Box as B

MOVE_MAP = {'^': [0,-1], '>': [1,0], 'v': [0,1], '<': [-1,0]}

def can_push_boxes(box, boxes, walls, move_dir):
    new_spot = [box[0] + move_dir[0], box[1] + move_dir[1]]
    if new_spot in walls:
        return False
    elif new_spot in boxes:
        return can_push_boxes(new_spot, boxes, walls, move_dir)
    else:
        return True


def push_boxes(box, boxes, walls, move_dir):
    if can_push_boxes(box, boxes, walls, move_dir):
        done = False
        new_boxes = {}
        while not done:
            new_spot = [box[0] + move_dir[0], box[1] + move_dir[1]]
            i = boxes.index(box)
            if new_spot not in boxes:
                i = boxes.index(box)
                boxes[i] = new_spot
                done = True
            else:
                new_boxes[i] = new_spot
                box = new_spot

        for k,v in new_boxes.items():
            boxes[k] = v

        return True, boxes

    return False, boxes


def move(robot, boxes, walls, instruction):
    move_dir = MOVE_MAP[instruction]

    new_spot = [robot.x + move_dir[0], robot.y + move_dir[1]]
    if new_spot in walls:
        return robot, boxes
    
    if new_spot in boxes:
        did_push, boxes = push_boxes(new_spot, boxes, walls, move_dir)
        if did_push:
            robot.x = new_spot[0]
            robot.y = new_spot[1]
    else:
        robot.x = new_spot[0]
        robot.y = new_spot[1]
    
    return robot, boxes
    

def part1(room, instructions):
    total = 0

    boxes = []
    walls = []
    robot = None
    for y, row in enumerate(room):
        for x, col in enumerate(row):
            if col == '@':
                robot = P(x,y)
            elif col == '#':
                walls.append([x,y])
            elif col == 'O':
                boxes.append([x,y])

    for instruction in instructions:
        robot, boxes = move(robot, boxes, walls, instruction)

    for box in boxes:
        total += (box[1] * 100 + box[0])

    return total

def find_a_box(pos, boxes):
    for box in boxes:
        if box.l.x == pos[0] and box.l.y == pos[1]:
            return box
        if box.r.x == pos[0] and box.r.y == pos[1]:
            return box
        
    return None

def push_boxes_2(box_being_pushed, boxes, walls, move_dir, moved_boxes=[]):
    del boxes[boxes.index(box_being_pushed)]
    box_being_pushed.l.x += move_dir[0]
    box_being_pushed.l.y += move_dir[1]
    box_being_pushed.r.x += move_dir[0]
    box_being_pushed.r.y += move_dir[1]
    moved_boxes.append(box_being_pushed)
    
    next_pos_l = [box_being_pushed.l.x, box_being_pushed.l.y]
    next_pos_r = [box_being_pushed.r.x, box_being_pushed.r.y]
    if next_pos_l in walls or next_pos_r in walls:
        return False, boxes, moved_boxes
    
    boxes_to_push = []

    next_box_l = find_a_box(next_pos_l, boxes)
    if next_box_l:
        if next_box_l not in boxes_to_push:
            boxes_to_push.append(next_box_l)
        
    next_box_r = find_a_box(next_pos_r, boxes)
    if next_box_r:
        if next_box_r not in boxes_to_push:
            boxes_to_push.append(next_box_r)
    
    for b in boxes_to_push:
        blow_it_up, _, _ = push_boxes_2(b, boxes, walls, move_dir, moved_boxes)
        if not blow_it_up:
            return False, boxes, moved_boxes
    
    return True, boxes, moved_boxes


def move_robot(robot, boxes, walls, instruction):
    move_dir = MOVE_MAP[instruction]

    new_spot = [robot.x + move_dir[0], robot.y + move_dir[1]]
    if new_spot in walls:
        return robot, boxes
    if find_a_box(new_spot, boxes):
        did_push, boxes, moved_boxes = push_boxes_2(find_a_box(new_spot, boxes), boxes, walls, move_dir, [])
        if did_push:
            robot.x = new_spot[0]
            robot.y = new_spot[1]
            for box in moved_boxes:
                boxes.append(box)
        else:
            for box in moved_boxes:
                box.l.x -= move_dir[0]
                box.l.y -= move_dir[1]
                box.r.x -= move_dir[0]
                box.r.y -= move_dir[1]
                boxes.append(box)
    else:
        robot.x = new_spot[0]
        robot.y = new_spot[1]
    
    return robot, boxes

def part2(room, instructions):
    total = 0

    boxes = []
    walls = []
    robot = None
    for y, row in enumerate(room):
        for x, col in enumerate(row):
            if col == '@':
                robot = P(x,y)
            elif col == '#':
                walls.append([x,y])
            elif col == '[':
                boxes.append(B(P(x,y),P(x+1,y)))

    for i, instruction in enumerate(instructions):
        print(f"Instruciton: {instruction} which is {i}th")
        robot, boxes = move_robot(robot, boxes, walls, instruction)

    for box in boxes:
        total += (box.l.y * 100 + box.l.x)

    return total

def run(file_name):
    is_part1 = False

    if is_part1:
        room = []
        instructions = ''
        
        on_grid = True
        with open(file_name, 'r') as file:
            for line in file:
                if len(line) == 1:
                    on_grid = False
                elif on_grid:
                    line_list = list(line.replace('\n', ''))
                    room.append(line_list)
                else:
                    instructions += line.replace('\n', '')

        result1 = part1(room, instructions)
        print(f"Day 15 - Part 1: {result1}")
    else:
        room = []
        instructions = ''
        
        on_grid = True
        with open(file_name, 'r') as file:
            for line in file:
                if len(line) == 1:
                    on_grid = False
                elif on_grid:
                    line_list = list(line.replace('\n', ''))
                    tmp_line = ''
                    for l in line_list:
                        if l == '#':
                            tmp_line += '##'
                        elif l == '.':
                            tmp_line += '..'
                        elif l == '@':
                            tmp_line += '@.'
                        elif l == 'O':
                            tmp_line += '[]'
                    room.append(list(tmp_line))
                else:
                    instructions += line.replace('\n', '')

        result2 = part2(room, instructions)
        
        print(f"Day 15 - Part 2: {result2}")
