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

def is_solid(x, y):
    if y == 0:
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
            elif y == 0:
                print('-', end='')
            else:
                print('.', end='')
        print()
    print()


def simulate_rock(r):
    global i
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
        i += 1 
        # move down
        for x, y in r:
            if is_solid(x, y - 1):
                stationary = True
                for x, y in r:
                    solid.add((x, y))
                break
        if not stationary:
            r = [(x, y - 1) for x, y in r]
    return r

amount_of_rocks = 2022
highest_y = 0
for n in range(amount_of_rocks):
    new_rock = []
    for y, row in enumerate(rocks_types[current_rock_type]):
        for x in row:
            new_rock.append((spawn_x + x, y + highest_y + 4))
    simulate_rock(new_rock)
    current_rock_type = (current_rock_type + 1) % len(rocks_types)
    highest_y = max(y for x, y in solid)
    
    
print(highest_y)