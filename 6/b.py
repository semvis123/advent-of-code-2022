from inp import inputData

def findStartMarker(text):
    last14 = text[:14]
    i = 0
    while len(last14) != len(set(last14)):
        i+=1
        last14 = text[i:i+14]
    return i + 14
print(findStartMarker(inputData))