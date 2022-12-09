from inp import inputData
from pprint import pprint


class Tree:
    def __init__(self, height, position):
        self.height = height
        self.position = position

    def __gt__(self, other):
        return self.height > other.height
    def __ge__(self, other):
        return self.height >= other.height
    
trees = [[Tree(int(x), (i, j)) for j, x in enumerate(row)] for i, row in enumerate(inputData)]


def count_from_left(table):
    visible_trees = set()
    for row in table:
        index = 0
        previous = 0
        current = row[0]
        while True:
            if previous == 0 or current > previous:
                visible_trees.add(current)
            index += 1
            if previous == 0 or current > previous:
                previous = current
            if index == len(row):
                break
            current = row[index]
    return visible_trees            

total_visible_trees = set()
total_visible_trees |= count_from_left(trees)
total_visible_trees |= count_from_left(x[::-1] for x in trees)
total_visible_trees |= count_from_left(list(zip(*trees)))
total_visible_trees |= count_from_left(x[::-1] for x in list(zip(*trees)))



def print_trees_at_position(trees):
    grid_size = len(inputData)
    for i in range(grid_size):
        for j in range(grid_size):
            for tree in trees:
                if tree.position == (i, j):
                    print(tree.height, end='')
                    break
            else:
                print('.', end='')
        print()

print_trees_at_position(total_visible_trees)
print(len(total_visible_trees))