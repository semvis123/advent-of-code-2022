from inp import inputData

class Node:
    def __init__(self, name, type='dir', parent=None, size=0):
        self.name = name
        self.type = type
        self.size = size
        self.children = []
        self.parent = parent

file_tree = Node('root')
current = file_tree
for line in inputData:
    if line[0] == '$':
        # command
        if line[:4] == '$ cd':
            if line[4:].strip() == '..':
                current = current.parent
                continue
            # change directory
            new_directory = Node(line[4:].strip(), 'dir', current)
            current.children.append(new_directory)
            current = new_directory
        continue
    elif line[:3] == 'dir':
        continue
    size, filename = line.split()
    new_file = Node(filename, 'file', current, int(size))
    current.size += new_file.size
    current.children.append(new_file)
    
    current_parent = current.parent
    while current_parent:
        current_parent.size += new_file.size
        current_parent = current_parent.parent

def print_each(node, depth=0):
    print("  "*depth, node.name, node.size)
    for child in node.children:
        print_each(child, depth+1)

def flatten(node):
    return [node] + [x for child in node.children for x in flatten(child)]


print_each(file_tree)

print(list(x.size for x in flatten(file_tree) if x.size < 100000 and x.type == 'dir'))