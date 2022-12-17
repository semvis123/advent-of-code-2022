import math
from inp import inputData, testData

data = inputData

current_rock_type = 0
rocks_types = [
    [[0, 1, 2, 3]],
    [[1], [0, 1, 2], [1]],
    [[2], [2], [0, 1, 2]],
    [[0], [0], [0], [0]],
    [[0, 1], [0, 1]]
]

rocks_types = [x[::-1] for x in rocks_types]

width = 7
movement_chars = {
    '<': -1,
    '>': 1,
}
spawn_x = 2
solid = set()
movement = data
i = 0
highest_floor = 0
floor = [0] * width
floors = [(0, tuple(floor))]
floor_locations = {}

def is_solid(x, y):
    if y == highest_floor:
        return True
    if x < 0 or x >= width:
        return True
    if (x, y) in solid:
        return True
    return False
        
def print_state_rock(r):
    for y in range(highest_y + 5, -1, -1):
        for x in range(width):
            if (x, y) in solid:
                print('#', end='')
            elif (x, y) in r:
                print('O', end='')
            elif y == highest_floor:
                print('-', end='')
            else:
                print('.', end='')
        print()
    print()


def simulate_rock(r):
    global i, highest_floor, solid, floor, floors, current_rock_type, n, amount_of_rocks
    
    stationary = False
    while not stationary:
        # move left right
        direction = movement_chars[movement[i % len(movement)]]
        can_move = True
        for x, y in r:
            if is_solid(x + direction, y):
                can_move = False
                break
        if can_move:
            r = [(x + direction, y) for x, y in r]
        i = (i+1) % len(movement)
        # move down
        for x, y in r:
            if is_solid(x, y - 1):
                stationary = True
                for x, y in r:
                    solid.add((x, y))
                break
        if not stationary:
            r = [(x, y - 1) for x, y in r]
        else:
            deepest_floor = math.inf
            for x in range(width):
                check_y = r[0][1]
                while not is_solid(x, check_y):
                    check_y -= 1
                deepest_floor = min(check_y, deepest_floor)
                floor[x] = check_y
            highest_floor = deepest_floor - 2
            solid = set((x, y) for x, y in solid if y > highest_floor)
            # save floor layout
            floor = [x - highest_floor for x in floor]
            floor_item = (i, tuple(floor), current_rock_type)
            if floor_item in floors:
                to_go = amount_of_rocks - n
                height = highest_floor - floor_locations[floor_item][0]
                n_height = (n - floor_locations[floor_item][1])
                skip_n = (to_go // n_height)
                n += skip_n * n_height
                solid = set((x, y + height * skip_n) for x, y in solid)
                highest_floor += height * skip_n
            else:
                floors += [floor_item]
                floor_locations[floor_item] = highest_floor, n
    return r

amount_of_rocks = 1_000_000_000_000
highest_y = 0


n = 0
while n < amount_of_rocks:
    new_rock = []
    for y, row in enumerate(rocks_types[current_rock_type]):
        for x in row:
            new_rock.append((spawn_x + x, y + highest_y + 4))
    # print(new_rock)
    simulate_rock(new_rock)
    current_rock_type = (current_rock_type + 1) % len(rocks_types)
    highest_y = max(y for x, y in solid)
    # print_state_rock([])
    n += 1
    # print(n)
    
print(highest_y)
