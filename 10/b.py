from inp import inputData

cycle_n = 1
reg_x = 1

def cycle_check(c, x):
    sprite = '.' * (x - 1) + '###' + '.' * (38 - x)
    print(sprite[(c-1)%40], end='')
    if c % 40 == 0:
        print()


def cycle(command):
    global reg_x, cycle_n
    cycle_check(cycle_n, reg_x)

    if command[0] == 'noop':
        cycle_n += 1
    
    if command[0] == 'addx':
        cycle_n += 1
        cycle_check(cycle_n, reg_x)
        cycle_n += 1
        reg_x += int(command[1])
    
    
for i, line in enumerate(inputData):
    cycle(line)

