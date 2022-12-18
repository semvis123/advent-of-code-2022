from inp import testData, inputData, smallTestData

data = inputData

space = [[[0 for _ in range(30)] for _ in range(30)] for _ in range(30)]

for x, y, z in data:
    current = (x, y, z)
    space[x][y][z] = current

surface_area = 0


to_visit = [(-1,-1,-1)]
directions = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
visited = set()
counted_faces = set()
while to_visit:
    current = to_visit.pop()
    visited.add(current)
    if min(current) < -1 or max(current) > 20:
        continue
    
    for d in directions:
        next = (current[0] + d[0], current[1] + d[1], current[2] + d[2])
        if space[next[0]][next[1]][next[2]] != 0:
            if (d, next) not in counted_faces:
                surface_area += 1
                counted_faces.add((d, next))
        else:
            if next not in visited:
                to_visit.append(next)

print(surface_area)