from typing import List, Tuple
import re

def parse_input() -> List[Tuple[int]]:
    operations = []
    with open('input.txt') as f:
        input = f.read() 
    
    for sub in re.split(r"do\(\)", input):
        instructions_to_execute = re.split(r"don\'t\(\)", sub)[0]
        raw_operations = re.findall(r"(mul\(\d{1,3},\d{1,3}\))", instructions_to_execute)
        for operation in raw_operations:
            a,b = re.search(r"mul\((\d{1,3}),(\d{1,3})\)", operation).groups()
            operations.append((int(a), int(b)))

    return operations

def compute(operations: List[Tuple[int]]) -> int:
    total = 0
    while operations:
        a,b = operations.pop()
        total += a * b
    return total

if __name__ == '__main__':
    operations = parse_input()
    result = compute(operations)
    print(f'Total is {result}')
