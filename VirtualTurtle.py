def turtle(coord, direction):
    command = ''
    actual_coord = list(coord)
    actual_direction = direction
    
    while True:
        command = yield tuple(actual_coord)
        if command == 'f':
            if actual_direction == 0:
                actual_coord[0] += 1
            elif actual_direction == 1:
                actual_coord[1] += 1
            elif actual_direction == 2:
                actual_coord[0] -= 1
            elif actual_direction == 3:
                actual_coord[1] -= 1
        elif command == 'l':
            actual_direction = (actual_direction + 1) % 4
        elif command == 'r':
            actual_direction = (actual_direction - 1) % 4
