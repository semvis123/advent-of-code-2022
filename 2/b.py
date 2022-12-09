from inp import inputData

rps = {
    'A': 1, # rock
    'B': 2, # paper
    'C': 3, # scissors
    'X': 1,
    'Y': 2,
    'Z': 3,
}

winMap = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

loseMap = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}


def scoreGame(a, b):
    if rps[a] == rps[b]:
        # draw
        return rps[b] + 3
    if rps[a] == rps[b] + 1 or rps[a] == rps[b] - 2:
        # a wins
        return rps[b] + 0
    return rps[b] + 6

def score(a, b):
    if b == 'X':
        # pick to lose
        return scoreGame(a, loseMap[a])
    if b == 'Y':
        # pick to draw
        return scoreGame(a, a)
    if b == 'Z':
        # pick to win
        return scoreGame(a, winMap[a])

print(score('A', 'Y'))
print(score('B', 'X'))
print(score('C', 'Z'))

print(sum(score(*x) for x in inputData))