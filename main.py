from utils import read_command_line, part1, part2

if __name__ == '__main__':
    with open('command_line.txt', 'r') as command_line:
        command_line = [line.strip('\n') for line in command_line]

    occupied, directories = read_command_line(command_line)
    solution1 = part1(directories, 100_000)
    solution2 = part2(directories, 70_000_000, occupied, 30_000_000)
    print(f'The sum of all sub-100,000 memory directories is {solution1}')
    print(f'The smallest directory of sufficient size for update is {solution2}')
    