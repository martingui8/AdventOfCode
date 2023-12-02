def parse_line(line: str) -> int:
    i,j = 0,-1
    while not line[i].isnumeric():
        i += 1
    while not line[j].isnumeric():
        j -= 1
    return int(f'{line[i]}{line[j]}')

if __name__ == '__main__':
    f = open('input.txt')
    print(sum(map(parse_line, f.readlines())))
