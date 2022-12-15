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
space_used_set = list()
beacons = set()

data = inputData
check_y = 2000000 if data == inputData else 10
for sensor, closest_beacon in data:
    distance_x, distance_y = abs(sensor[0] - closest_beacon[0]), abs(sensor[1] - closest_beacon[1])
    distance = distance_x + distance_y
    
    if abs(check_y - sensor[1]) > distance:
        continue

    y_range = (distance - abs(check_y - sensor[1]))

    space = (sensor[0] - y_range, sensor[0] + y_range)
    space = sorted(space)

    space_used_set.append(space)
    beacons.add(tuple(closest_beacon))

count_at_y = 0
remove_overlaps(space_used_set)
for space in space_used_set:
    count_at_y += space[1] - space[0] + 1
    print(space)

for beacon in beacons:
    if beacon[1] == check_y:
        for space in space_used_set:
            if space[0] <= beacon[0] <= space[1]:
                count_at_y -= 1
                break

if data == testData:
    assert count_at_y == 26, count_at_y
if data == inputData:
    assert count_at_y == 4883971, count_at_y
print(count_at_y)