from functools import reduce
from inp import monkeys
import operator

operators = {
    '*': operator.mul,
    '+': operator.add
}

def next_round(monkeys):
    for monkey in monkeys:
        while len(monkey['items']) > 0:
            monkey['inspection'] = monkey.get('inspection', 0) + 1
            item = monkey['items'].pop(0)

            new_item = monkey['operation'][1](
                item if isinstance(monkey['operation'][0], str) else monkey['operation'][0],
                item if isinstance(monkey['operation'][2], str) else monkey['operation'][2]
            )
            
            new_item //= 3
            
            if new_item % monkey['test'] == 0:
                monkeys[monkey['if_true']]['items'].append(new_item)
            else:
                monkeys[monkey['if_false']]['items'].append(new_item)
            
    return monkeys

for i in range(20):
    monkeys = next_round(monkeys)

# for monkey in monkeys:
#     print(monkey['inspection'])
#     print(monkey['items'])

print(reduce(lambda x, y: x * y, sorted(m['inspection'] for m in monkeys)[-2:], 1))