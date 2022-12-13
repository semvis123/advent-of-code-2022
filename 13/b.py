from functools import cmp_to_key
from inp import inputData, testData



def a_smaller_than_b(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return 1 if a < b else (-1 if a > b else 0)
    if isinstance(a, list) and isinstance(b, list):
        for i in range(len(a)): 
            if i >= len(b):
                return -1
            result = a_smaller_than_b(a[i], b[i])
            if result != 0:
                return result
        if len(a) < len(b):
            return 1
        return 0
    if isinstance(a, int):
        return a_smaller_than_b([a], b)
    return a_smaller_than_b(a, [b])

flattened_list = [item for sublist in inputData for item in sublist]
flattened_list += [[[2]]]
flattened_list += [[[6]]]
# print(sum(i+1 for i, pair in enumerate(inputData) if a_smaller_than_b(*pair) == 1))

sortedData = sorted(flattened_list, key=cmp_to_key(lambda a, b: -a_smaller_than_b(a, b)))
print((sortedData.index([[2]]) + 1) *( sortedData.index([[6]]) + 1))

# for pair in inputData:
#     print(pair[0], pair[1])
#     print(a_smaller_than_b(pair[0], pair[1]))
    
assert a_smaller_than_b(*testData[0]) == 1, testData[0]
assert a_smaller_than_b(*testData[1]) == 1, testData[1]
assert a_smaller_than_b(*testData[2]) == -1, testData[2]
assert a_smaller_than_b(*testData[3]) == 1, testData[3]
assert a_smaller_than_b(*testData[4]) == -1, testData[4]
assert a_smaller_than_b(*testData[5]) == 1, testData[5]
assert a_smaller_than_b(*testData[6]) == -1, testData[6]
assert a_smaller_than_b(*testData[7]) == -1, testData[7]

