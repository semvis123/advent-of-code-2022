from inp import stacks, moves

def rearrange(stacks, move):
    stacks[move['to']] += stacks[move['from']][-move['amount']:][::-1]
    stacks[move['from']] = stacks[move['from']][:-move['amount']]
    return stacks

for move in moves:
    stacks = rearrange(stacks, move)

for stack in stacks.values():
    print(stack[-1], end='')
print()
    