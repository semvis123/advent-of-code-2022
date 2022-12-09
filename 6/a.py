from inp import inputData

def findStartMarker(text):
    last4 = text[:4]
    i = 0
    while len(last4) != len(set(last4)):
        i+=1
        last4 = text[i:i+4]
    return i + 4
print(findStartMarker(inputData))