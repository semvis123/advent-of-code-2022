from inp import inputData

def a_contains_b(a, b):
    return b[0] >= a[0] and b[1] <= a[1]

def contains(a, b):
    a, b = sorted(a), sorted(b)
    return a_contains_b(a, b) or a_contains_b(b, a)


print(sum(contains(*pair) for pair in inputData))