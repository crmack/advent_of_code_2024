def valid_pos(x, y, size_x, size_y):
    if x >= 0 and y >= 0 and x < size_x and y < size_y:
        return True
    
    return False