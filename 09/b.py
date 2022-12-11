from inp import inputData

class Knot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.head = None
        self.tail = None

    def is_touching(self, tail):
        if self == tail:
            return True
        if abs(self.x - tail.x) <= 1 and abs(self.y - tail.y) <= 1:
            return True
        return False
    
    def move(self, direction):
        if self.head is None:
            self.x += direction[0]
            self.y += direction[1]
            self.tail.move(direction)
            return self
        
        if self.is_touching(self.head):
            if self.tail is not None:
                self.tail.move(direction)
            return self
        
        if self.x != self.head.x and self.y != self.head.y:
            # diagonal
            diagonal = ([1,-1][self.x > self.head.x], [1,-1][self.y > self.head.y])
            self.x += diagonal[0]
            self.y += diagonal[1]
        else:
            # horizontal or vertical
            if abs(self.x - self.head.x) > 1:
                self.x += [1,-1][self.x > self.head.x]
            if abs(self.y - self.head.y) > 1:
                self.y += [1,-1][self.y > self.head.y]
                
        if self.tail is not None:
            self.tail.move(direction)
        
        return self

    def position(self):
        return (self.x, self.y)
    
knots = [Knot(0,0) for _ in range(10)]
for i in range(1, len(knots)):
    knots[i].head = knots[i-1]
    knots[i-1].tail = knots[i]
visited = set()

directions = {
    'R': (1,0),
    'L': (-1,0),
    'U': (0,1),
    'D': (0,-1)
}

def print_state():
    knot_pos = list(map(lambda x: x.position(), knots))
    for y in range(10, -10, -1):
        for x in range(-10, 10):
            if (x,y) == knot_pos[0]:
                print('H', end='')
            elif (x,y) in knot_pos:
                print(knot_pos.index((x, y)), end='')
            else:
                print('.', end='')
        print()
    print()

for direction, amount in inputData:
    direction = directions[direction]
    for _ in range(amount):
        knots[0].move(direction)
        visited.add(knots[-1].position())
        # print_state()
print(len(visited))