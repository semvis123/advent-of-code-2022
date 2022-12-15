from inp import inputData, testData

assert testData[0][0] == [2, 18], testData[0][0]
assert testData[0][1] == [-2, 15], testData[0][1]

def remove_overlaps(overlaps):
    for i, overlap in enumerate(overlaps):
        for j, overlap2 in enumerate(overlaps):
            if i != j:
                x1, x2 = sorted(overlap)
                x3, x4 = sorted(overlap2)
                # if there is an overlap, adjust the first one, and remove the second one
                if x1 <= x3 <= x2 or x1 <= x4 <= x2:
                    overlaps[i] = (min(x1, x3), max(x2, x4))
                    overlaps.pop(j)
                    return remove_overlaps(overlaps)
                
    return overlaps

assert remove_overlaps([(1, 2), (2, 3)]) == [(1, 3)], remove_overlaps([(1, 2), (2, 3)])
assert remove_overlaps([(1, 1), (2, 3)]) == [(1, 1), (2, 3)], remove_overlaps([(1, 1), (2, 3)])
assert remove_overlaps([(1, 2), (2, 3), (3, 4)]) == [(1, 4)], remove_overlaps([(1, 2), (2, 3), (3, 4)])
assert remove_overlaps([(-2, 6), (-1, 1), (1, 11)]) == [(-2, 11)], remove_overlaps([(-2, 6), (-1, 1), (1, 11)])
assert remove_overlaps([(15, 13), (13, 15)]) == [(13, 15)], remove_overlaps([(15, 13), (13, 15)])
beacons = set()
used_space_at_y = {}

data = inputData

max_coord = 4000000 if data == inputData else 20
for sensor, closest_beacon in data:
    distance_x, distance_y = abs(sensor[0] - closest_beacon[0]), abs(sensor[1] - closest_beacon[1])
    distance = distance_x + distance_y
    

    for y in range(sensor[1] - distance, sensor[1] + distance + 1):
        if abs(y - sensor[1]) > distance:
            continue
        if not (0 <= y <= max_coord):
            continue
        y_range = (distance - abs(y - sensor[1]))

        space = (sensor[0] - y_range, sensor[0] + y_range)
        space = sorted(space)
        space[0] = max(0, space[0])
        space[1] = min(max_coord, space[1])

        used_space_at_y[y] = used_space_at_y.get(y, []) + [tuple(space)]
        beacons.add(tuple(closest_beacon))

# for b in beacons:
#     used_space_at_y[b[1]] = used_space_at_y.get(b[1], y) + [b[0], b[0]]

for check_y, space_used in used_space_at_y.items():
    remove_overlaps(space_used)
    # for space in space_used:
    #     # check if there is a value in this space where x * y + y
    if len(space_used) > 1:
        print((space_used[0][1] + 1) * max_coord + check_y)
        # print(space_used)
        # print(check_y)
