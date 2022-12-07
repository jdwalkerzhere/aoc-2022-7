class directory:
    def __init__(self, parent = None):
        self.parent = parent
        self.children = {}
        self.size = 0

def read_command_line(lines):
    root = directory()
    curr_dir = root
    # Dir Sizes holds all directories sizes
    dir_sizes = []
    for line in lines:
        curr_line = line.split()
        if curr_line[0] == '$' and curr_line[1] == 'cd':
            # Return to Root command
            if curr_line[2] == '/':
                while curr_dir.parent:
                    curr_dir.parent.size += curr_dir.size
                    curr_dir = curr_dir.parent
            # Return to Previous Directory Command
            if curr_line[2] == '..':
                dir_sizes.append(curr_dir.size)
                curr_dir.parent.size += curr_dir.size
                curr_dir = curr_dir.parent
            # Move into New Directory Command
            else:
                curr_dir.children[curr_line[2]] = directory(parent=curr_dir)
                curr_dir = curr_dir.children[curr_line[2]]
        # ls Command
        elif curr_line[0] == '$': continue
        # Read and add file size
        elif curr_line[0] != 'dir':
            curr_dir.size += int(curr_line[0])
    root = root.children['/'].size
    # Return Total Size and All Sub-Directory sizes
    return root, dir_sizes

def part1(li_of_sizes, max_size):
    return sum([size for size in li_of_sizes if size <= max_size])

def part2(li_of_sizes, os_size, occupied_mem, needed_size):
    need = abs((os_size - occupied_mem) - needed_size)
    return sorted([size for size in li_of_sizes if size >= need])[0]
    
