class directory:
    def __init__(self, parent = None):
        self.parent = parent
        self.children = {}
        self.size = 0

def read_command_line(lines):
    root = directory()
    curr_dir = root
    dir_sizes, previous_dirs = [], []
    for line in lines:
        curr_line = line.split()
        if curr_line[0] == '$' and curr_line[1] == 'cd':
            if curr_line[2] == '/':
                while previous_dirs:
                    previous_dirs[-1].size += curr_dir.size
                    curr_dir = previous_dirs[-1]
                    previous_dirs.pop()
            if curr_line[2] == '..':
                dir_sizes.append(curr_dir.size)
                previous_dirs[-1].size += curr_dir.size
                curr_dir = previous_dirs[-1]
                previous_dirs.pop()
            else:
                curr_dir.children[curr_line[2]] = directory(parent=curr_dir)
                previous_dirs.append(curr_dir)
                curr_dir = curr_dir.children[curr_line[2]]
        elif curr_line[0] == '$': continue
        elif curr_line[0] != 'dir':
            curr_dir.size += int(curr_line[0])
    root = root.children['/'].size
    return root, dir_sizes

def part1(li_of_sizes, max_size):
    return sum([size for size in li_of_sizes if size < max_size])

def part2(li_of_sizes, os_size, occupied_mem, needed_size):
    diff = abs((os_size - occupied_mem) - needed_size)
    return sorted([size for size in li_of_sizes if size >= diff])[0]
    
