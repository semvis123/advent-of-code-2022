from inp import inputData

head = (0,0)
tail = (0,0)

visited = set()

directions = {
    'R': (1,0),
    'L': (-1,0),
    'U': (0,1),
    'D': (0,-1)
}


def is_touching(head, tail):
    if head == tail:
        return True
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return True
    return False

def print_state():
    for y in range(6, -1, -1):
        for x in range(0, 6):
            if (x,y) == head:
                print('H', end='')
            elif (x,y) == tail:
                print('T', end='')
            elif (x,y) in visited:
                print('X', end='')
            else:
                print('.', end='')
        print()
    print()

for direction, amount in inputData:
    direction = directions[direction]
    for _ in range(amount):
        head = (head[0] + direction[0], head[1] + direction[1])
        if not is_touching(head, tail):
            tail = head
            tail = (tail[0] - direction[0], tail[1] - direction[1])
        visited.add(tail)
        # print_state()
        
print(len(visited))