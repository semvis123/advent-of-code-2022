from functools import lru_cache
from inp import inputData, testData
from sys import setrecursionlimit

# sssst
setrecursionlimit(10000)

data = inputData
sand_source = (500,0)
sand = []
grid = []

# fixes the slow method lol
@lru_cache(maxsize=None)
def check_if_solid(x, y):
    for path in data:
        prev = path[0]
        for point in path[1:]:
            if prev[0] <= x <= point[0] and prev[1] <= y <= point[1]:
                return True
            if point[0] <= x <= prev[0] and point[1] <= y <= prev[1]:
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
        if not check_if_solid(*new_sand) and not new_sand in sand:
            sand.append(new_sand)
            sand.remove(s)
            return move_sand(data) if s[1] < 170 else False
    return True

            
while place_sand(data):
    # print_state(data)
    pass
print(len(sand) - 1)