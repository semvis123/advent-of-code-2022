from inp import inputData

def a_overlaps_b(a, b):
    return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]

def overlaps(a,b):
    return a_overlaps_b(a, b) or a_overlaps_b(b, a)

print(sum(overlaps(*pair) for pair in inputData))