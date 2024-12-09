from typing import List, Tuple, Callable, Iterator

def parse_input() -> List[Tuple[int,List[int]]]:
    tests = []
    with open('input.txt') as f:
        line = f.readline() 
        while line:
            result, _, numbers = line.partition(':')
            tests.append((int(result), [int(i.strip()) for i in numbers.split()]))
            line = f.readline() 
    return tests

def operation(left: int, operator: str, right: int) -> int:
    if operator == '+':
        return left + right
    if operator == '*':
        return left * right
    if operator == '||':
        return int(str(left) + str(right))
    raise Exception(f'Unknown operator: {operator}')

def compute(numbers: List[int], operators: List[str]) -> int:
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = operation(result, operators[i - 1], numbers[i])
    return result

def make_operators_generator(size: int) -> Callable[[], Iterator[List[int]]]:
    def operations_generator() -> Iterator[List[str]]:
        for i in range(3**size):
            L = []
            j = i
            while len(L) < size:
                L.append(['+', '*', '||'][j % 3])
                j = j // 3
            yield L
    return operations_generator()

if __name__ == '__main__':
    inputs = parse_input()
    total_calibration_result = 0
    for target, numbers in inputs:
        generator = make_operators_generator(len(numbers) - 1)
        for combination in generator:
            if compute(numbers, combination) == target:
                total_calibration_result += target 
                break
    print(f'Total calibration result: {total_calibration_result}')
