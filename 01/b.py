from inp import inputData

print(sum(sorted(sum(map(int, x)) for x in inputData)[::-1][:3]))