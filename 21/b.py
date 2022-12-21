import operator
from typing import Callable

monkeys = {}

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

invert_operators = {
    operator.add: operator.sub,
    operator.sub: operator.add,
    operator.mul: operator.floordiv,
    operator.floordiv: operator.mul,
} 


class Monkey:
    name: str
    value: int
    operation: Callable
    searched_human: bool
    depends_on_human: bool
    
    def __init__(self, name, value, left = None, right = None, operation = None):
        self.name = name
        self.value = value
        self.left = left
        self.right = right
        self.operation = operation
        self.searched_human = False
        self.depends_on_human = False
        
    def is_depending_on_human(self):
        if not self.searched_human:
            self.searched_human = True
            if self.name == 'humn':
                self.depends_on_human = True
            else:
                for monkey in [self.left, self.right]:
                    if monkey is None:
                        continue
                    if monkey.is_depending_on_human():
                        self.depends_on_human = True
                        break
        return self.depends_on_human

    def calc_value(self):
        if self.value is None:
            self.value = self.operation(self.left.calc_value(), self.right.calc_value())
        return self.value
    
    def find_value_of_human(self, value=None):
        if self.name == 'humn':
            return value
        
        if self.left is None and self.right is None:
            return self.value
        
        left_is_human_branch = self.left.is_depending_on_human()
        
        human_branch = self.left if left_is_human_branch else self.right
        other_branch = self.right if left_is_human_branch else self.left
        if value is None:
            return human_branch.find_value_of_human(other_branch.calc_value())
        else:
            if self.operation in [operator.add, operator.mul]:
                return human_branch.find_value_of_human(invert_operators[self.operation](value, other_branch.calc_value()))
            if self.operation in [operator.sub, operator.floordiv]:
                if left_is_human_branch:
                    return human_branch.find_value_of_human(invert_operators[self.operation](value, other_branch.calc_value()))
                else:
                    return human_branch.find_value_of_human(self.operation(other_branch.calc_value(), value))
        
for line in open(0):
    name, value = line.split(':')
    parts = value.split()
    if len(parts) == 3:
        parts[1] = operators[parts[1]]
        monkeys[name] = Monkey(name, None, parts[0], parts[2], parts[1])
    else:
        parts[0] = int(parts[0])
        monkeys[name] = Monkey(name, parts[0])
        
for monkey in monkeys.values():
    monkey.left = monkeys[monkey.left] if monkey.left else None
    monkey.right = monkeys[monkey.right] if monkey.right else None
    

print(monkeys['root'].find_value_of_human())
