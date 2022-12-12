from inp import inputData
from string import ascii_lowercase
import sys

sys.setrecursionlimit(10000)

start = None
end = None

class Node:
    def __init__(self, x, y, val, parent):
        self.x = x
        self.y = y
        self.val = val
        self.parent = parent
    def __repr__(self):
        return f'Node({self.x}, {self.y}, {self.val}, {self.parent})'
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))
    
    def distance(self):
        if self.parent is None:
            return 0
        return self.parent.distance() + 1
    
    def cost(self):
        if self.val in ascii_lowercase:
            return len(ascii_lowercase) - ascii_lowercase.index(self.val)
        return len(ascii_lowercase)
    
    def print_path(self):
        if self.parent is None:
            return ''
        return self.parent.print_path() + self.val

for y, row in enumerate(inputData):
    for x, val in enumerate(row):
        if val == 'E':
            start = Node(x, y, val, None)

visited = set()
to_visit = [start]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while to_visit:
    current = to_visit.pop(0)
    if current.val in ['a', 'S']:
        break
    if current in visited:
        continue
    visited.add(current)
    for dx, dy in directions:
        x = current.x + dx
        y = current.y + dy
        if 0 <= y < len(inputData) and 0 <= x < len(inputData[0]):
            if current.val in ascii_lowercase and inputData[y][x] in ascii_lowercase and \
                ascii_lowercase.index(inputData[y][x]) < ascii_lowercase.index(current.val) - 1:
                continue
            next = Node(x, y, inputData[y][x], current)
            if current.val == 'E' and ascii_lowercase.index(next.val) < len(ascii_lowercase) - 1:
                continue
            if current.val in ['a', 'S'] and ascii_lowercase.index(current.val) > len(ascii_lowercase) + 1:
                continue
            to_visit.append(next)
    to_visit.sort(key=lambda n: n.cost())

print(current.distance())
