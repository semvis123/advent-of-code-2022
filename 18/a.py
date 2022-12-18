from inp import testData, inputData, smallTestData
import numpy as np


data = inputData

class Cube:
    position: tuple
    top: bool = True
    bottom: bool = True
    left: bool = True
    right: bool = True
    front: bool = True
    back: bool = True
    
    def __init__(self, position: tuple):
        self.position = position


cubes = set()
space = np.zeros((30, 30, 30)).tolist()

for x, y, z in data:
    current = Cube((x, y, z))
    cubes.add(current)
    space[x][y][z] = current
    
    if space[x][y][z - 1] != 0:
        space[x][y][z - 1].top = False
        current.bottom = False
    if space[x][y][z + 1] != 0:
        space[x][y][z + 1].bottom = False
        current.top = False
        
    if space[x][y - 1][z] != 0:
        space[x][y - 1][z].front = False
        current.back = False
    if space[x][y + 1][z] != 0:
        space[x][y + 1][z].back = False
        current.front  = False
        
    if space[x - 1][y][z] != 0:
        space[x - 1][y][z].right = False
        current.left = False
    if space[x + 1][y][z] != 0:
        space[x + 1][y][z].left = False
        current.right = False

surface_area = 0

for cube in cubes:
    faces = 0
    if cube.top: faces += 1
    if cube.bottom: faces += 1
    if cube.left: faces += 1
    if cube.right: faces += 1
    if cube.front: faces += 1
    if cube.back: faces += 1
    surface_area += faces

print(surface_area)
if data == smallTestData: assert surface_area == 10
if data == testData: assert surface_area == 64