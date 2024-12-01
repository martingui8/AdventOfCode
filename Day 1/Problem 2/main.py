import re

def parse_and_process_line(line: str) -> int:
    dig_map = {
        'one': 1,
        '1': 1,
        'two': 2,
        '2': 2,
        'three': 3,
        '3': 3,
        'four': 4,
        '4': 4,
        'five': 5,
        '5': 5,
        'six': 6,
        '6': 6,
        'seven': 7,
        '7': 7,
        'eight': 8,
        '8': 8,
        'nine': 9,
        '9': 9,
    }
    pattern = f"(?=({'|'.join(dig_map.keys())}))"
    matches = re.findall(pattern, line)
    res =  int(f'{dig_map[matches[0]]}{dig_map[matches[-1]]}')
    print(line, end='')
    print(res, end='\n\n')
    return res

if __name__ == '__main__':
    f = open('input.txt')
    print(sum(map(parse_and_process_line, f.readlines())))
    f.close()

