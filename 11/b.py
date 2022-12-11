from functools import reduce
import math
from inp import monkeys
import operator

lcm_all = math.lcm(*[m['test'] for m in monkeys])

def next_round(monkeys):
    for monkey in monkeys:
        while len(monkey['items']) > 0:
            monkey['inspection'] = monkey.get('inspection', 0) + 1
            item = monkey['items'].pop(0)
            
            new_item = monkey['operation'][1](
                item if isinstance(monkey['operation'][0], str) else monkey['operation'][0],
                item if isinstance(monkey['operation'][2], str) else monkey['operation'][2]
            ) % lcm_all
            
            monkey_to_update = monkey[('if_false', 'if_true')[new_item % monkey['test'] == 0]]
            monkeys[monkey_to_update]['items'].append(new_item)

    return monkeys

for i in range(10_000):
    monkeys = next_round(monkeys)

print(reduce(operator.mul, sorted(m['inspection'] for m in monkeys)[-2:], 1))