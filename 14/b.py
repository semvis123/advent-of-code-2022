from functools import lru_cache
from inp import inputData, testData
from sys import setrecursionlimit

# sssst
setrecursionlimit(10000)

data = inputData
sand_source = (500,0)
sand = []
grid = []


highest_y = 0
for path in data:
    for point in path:
        if point[1] > highest_y:
            highest_y = point[1]
print(highest_y)

# fixes the slow method lol
@lru_cache(maxsize=None)
def check_if_solid(pos):
    for path in data:
        prev = path[0]
        for point in path[1:]:
            if prev[0] <= pos[0] <= point[0] and prev[1] <= pos[1] <= point[1]:
                return True
            if point[0] <= pos[0] <= prev[0] and point[1] <= pos[1] <= prev[1]:
                return True
            prev = point
    return False

def print_state(data):
    for y in range(0, 10):
        for x in range(494, 504):
            if (x,y) in sand:
                print("+", end="")
            elif check_if_solid(x, y):
                print("#", end="")
            else:
                print(".", end="")
        print()


def place_sand(data):
    new_sand = sand_source
    if not new_sand in sand:
        sand.append(new_sand)
        return move_sand(data)
    return False

def move_sand(data):
    directions = (0,1), (-1,1), (1,1)
    s = sand[-1]
    for d in directions:
        new_sand = (s[0] + d[0], s[1] + d[1])
        if new_sand[1] > highest_y + 1:
            return True

        if not check_if_solid(new_sand) and not new_sand in sand:
            sand.append(new_sand)
            sand.remove(s)
            return move_sand(data)
    return True

i = 0    
while place_sand(data):
    # print_state(data)
    if i % 1000 == 0:
        print(len(sand))
    i+=1
print(len(sand))