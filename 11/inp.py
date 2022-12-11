inputData = """Monkey 0:
  Starting items: 63, 84, 80, 83, 84, 53, 88, 72
  Operation: new = old * 11
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 1:
  Starting items: 67, 56, 92, 88, 84
  Operation: new = old + 4
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 2:
  Starting items: 52
  Operation: new = old * old
  Test: divisible by 2
    If true: throw to monkey 3
    If false: throw to monkey 1

Monkey 3:
  Starting items: 59, 53, 60, 92, 69, 72
  Operation: new = old + 2
  Test: divisible by 5
    If true: throw to monkey 5
    If false: throw to monkey 6

Monkey 4:
  Starting items: 61, 52, 55, 61
  Operation: new = old + 3
  Test: divisible by 7
    If true: throw to monkey 7
    If false: throw to monkey 2

Monkey 5:
  Starting items: 79, 53
  Operation: new = old + 1
  Test: divisible by 3
    If true: throw to monkey 0
    If false: throw to monkey 6

Monkey 6:
  Starting items: 59, 86, 67, 95, 92, 77, 91
  Operation: new = old + 5
  Test: divisible by 19
    If true: throw to monkey 4
    If false: throw to monkey 0

Monkey 7:
  Starting items: 58, 83, 89
  Operation: new = old * 19
  Test: divisible by 17
    If true: throw to monkey 2
    If false: throw to monkey 1"""
    
    

# inputData = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1"""





inputData = [[y.split(': ')[1] for y in x.splitlines()[1:]] for x in inputData.split('\n\n')]
monkeys = [
    { 
     'items': [int(x) for x in monkeyData[0].split(', ')],
     'operation': monkeyData[1].split(' = ')[1],
     'test': int(monkeyData[2].split()[2]),
     'if_true': int(monkeyData[3].split()[3]),
     'if_false': int(monkeyData[4].split()[3])
    }
    for monkeyData in inputData
]

import operator
for m in monkeys:
    m['operation'] = m['operation'].split()
    if m['operation'][1] == '*':
        m['operation'][1] = operator.mul
    elif m['operation'][1] == '+':
        m['operation'][1] = operator.add
    if m['operation'][0].isnumeric():
        m['operation'][0] = int(m['operation'][0])
    if m['operation'][2].isnumeric():
        m['operation'][2] = int(m['operation'][2])
