def parse_path(wire_path):
    wire_path = wire_path.split(',')
    return [(mov[0], int(mov[1:])) for mov in wire_path]

def gather_crossed(wire1, wire2):
    curr_x = 0
    curr_y = 0
    coords = {}
    crossed = {}

    steps_taken = 0
    for (direction, dist) in wire1:
        while (dist > 0):
            if direction == 'R':
                curr_x += 1
            elif direction == 'L':
                curr_x += -1
            elif direction == 'U':
                curr_y += 1
            else: # D
                curr_y += -1

            steps_taken += 1
            coords[(curr_x, curr_y)] = steps_taken
            dist -= 1
    
    curr_x = 0
    curr_y = 0
    steps_taken = 0
    for (direction, dist) in wire2:
        while (dist > 0):
            if direction == 'R':
                curr_x += 1
            elif direction == 'L':
                curr_x += -1
            elif direction == 'U':
                curr_y += 1
            else: # D
                curr_y += -1

            steps_taken += 1
            if (curr_x, curr_y) in coords:
                crossed[(curr_x, curr_y)] = (coords[(curr_x, curr_y)] + steps_taken)
            dist -= 1

    return crossed

def manhattan_dist(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def main():
    paths = open('../data/day3.txt')
    wire1 = parse_path(paths.readline())
    wire2 = parse_path(paths.readline())
    paths.close()

    crossed = gather_crossed(wire1, wire2)

    min_dist = float('inf')
    for coords in crossed:
        dist = manhattan_dist((0,0), coords)
        min_dist = dist if dist < min_dist else min_dist

    answer1 = min_dist

    min_dist = float('inf')
    for coords in crossed:
        min_dist = crossed[coords] if crossed[coords] < min_dist else min_dist

    answer2 = min_dist

    return answer1


print(main())