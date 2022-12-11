from inp import inputData
from string import ascii_letters


def prio(x):
    return ascii_letters.index(x) + 1

print(sum(prio(list(set(rucksack[0]) & set(rucksack[1]))[0]) for rucksack in inputData))