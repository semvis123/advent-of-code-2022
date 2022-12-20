orig_file = []

for line in open(0):
    orig_file.append(int(line))

new_file_order = [x for x in range(len(orig_file))]

for i, n in enumerate(orig_file):
    curr = new_file_order.index(i)
    new_file_order.pop(curr)
    new_index = (curr + n - 1) % len(new_file_order) + 1
    new_file_order.insert(new_index, i)

new_file = [0] * len(new_file_order)
for x, y in enumerate(new_file_order):
    new_file[x] = orig_file[y]
print(new_file)

zero = new_file.index(0)
coords = [zero] * 3
coords[0] = new_file[(zero + 1000) % len(new_file)]
coords[1] = new_file[(zero + 2000) % len(new_file)]
coords[2] = new_file[(zero + 3000) % len(new_file)]

print(sum(coords))