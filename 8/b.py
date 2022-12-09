from inp import inputData

class Tree:
    def __init__(self, height, position, score = 0):
        self.height = height
        self.position = position
        self.score = score

    def __gt__(self, other):
        return self.height > other.height
    def __ge__(self, other):
        return self.height >= other.height
    
trees = [[Tree(int(x), (i, j)) for j, x in enumerate(row)] for i, row in enumerate(inputData)]

def scenic_score(tree, forest):
    score = 1
    score *= calculate_viewing_distance(tree, forest, (1, 0))
    score *= calculate_viewing_distance(tree, forest, (-1, 0))
    score *= calculate_viewing_distance(tree, forest, (0, 1))
    score *= calculate_viewing_distance(tree, forest, (0, -1))
    tree.score = score
    return score
    

def calculate_viewing_distance(tree, forest, direction):
    distance = 0
    while True:
        distance += 1
        position = (tree.position[0] + distance * direction[0],
                    tree.position[1] + distance * direction[1])
        
        if position[0] < 0 or position[1] < 0 or \
           position[0] >= len(forest) or position[1] >= len(forest):
            return distance - 1
        
        if forest[position[0]][position[1]] >= tree:
            return distance


best_tree = max(scenic_score(x, trees) for row in trees for x in row)
print(best_tree)