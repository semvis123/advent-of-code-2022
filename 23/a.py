elves = set()

d = {
    'N': -1j,
    'S': 1j,
    'E': 1,
    'W': -1,
    'NE': 1 - 1j,
    'NW': -1 - 1j,
    'SE': 1 + 1j,
    'SW': -1 + 1j,
}

all_moves = set(d.keys())

move_to = [
    ('N', {'N', 'NE', 'NW'}),
    ('S', {'S', 'SE', 'SW'}),
    ('W', {'W', 'NW', 'SW'}),
    ('E', {'E', 'NE', 'SE'}),
]

for y, line in enumerate(open(0)):
    for x, char in enumerate(line):
        if char == '#':
            elves.add(x + y * 1j)
            
# print(elves)

def print_room(room):
    min_x = min(elf.real for elf in room)
    min_y = min(elf.imag for elf in room)
    max_x = max(elf.real for elf in room)
    max_y = max(elf.imag for elf in room)
    # min_x = 0
    # min_y = 0
    # max_x = 10
    # max_y = 10
    print(min_x, min_y, max_x, max_y)
    print()
    for y in range(int(min_y), int(max_y) + 1):
        for x in range(int(min_x), int(max_x) + 1):
            print('#' if x + y * 1j in room else '.', end='')
        print()
    print()
    print()
    print()
        
# print_room(elves)



for i in range(10):
    old = elves.copy()
    moves = {}
    for elf in old:
        
        for move, moves_to_check in move_to:
            # print(elf, 'checking', move)
            can_move = True
            has_nearby_elf = False
            for m in all_moves.difference(moves_to_check):
                if (elf + d[m]) in old:
                    has_nearby_elf = True
                    break

            if not has_nearby_elf:
                continue
            
            for m in moves_to_check:
                if (elf + d[m]) in old:
                    can_move = False
                    break
            if can_move:
                if moves.get(elf + d[move]) is not None:
                    # mark as collision
                    moves[elf + d[move]] = (None, None)
                if moves.get(elf + d[move]) != (None, None):
                    moves[elf + d[move]] = elf
                break
        
    # print(moves)
    # print()
    # print(elves)
    for key, val in moves.items():
        if val != (None, None):
            elves.remove(val)
            elves.add(key)
    # print(len(elves))
    # print_room(elves)
    move_to = move_to[1:] + [move_to[0]]
    
min_x = min(elf.real for elf in elves)
min_y = min(elf.imag for elf in elves)
max_x = max(elf.real for elf in elves) + 1
max_y = max(elf.imag for elf in elves) + 1

# print(min_x, min_y, max_x, max_y)
answer = int((max_x - min_x) * (max_y - min_y)) - len(elves)
print(answer)

assert answer < 4415