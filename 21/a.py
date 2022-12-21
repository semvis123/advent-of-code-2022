import operator

monkeys = {}

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


for line in open(0):
    name, value = line.split(':')
    parts = value.split()
    if len(parts) == 3:
        parts[1] = operators[parts[1]]
    else:
        parts[0] = int(parts[0])
    monkeys[name] = parts
    
def resolve(monkey):
    if len(monkey) == 1:
        return monkey[0]
    else:
        return monkey[1](resolve(monkeys[monkey[0]]), resolve(monkeys[monkey[2]]))
    
print(resolve(monkeys['root']))