from typing import List, Dict
def parse_input() -> Dict[str, List[int]]:
    left, right = [], []
    with open('input.txt') as f:
        lines = map(
            lambda line: line.split(),
            f.readlines()
        )
        for l,r in lines:
            left.append(int(l.strip()))
            right.append(int(r.strip()))
    return {
        'left': left, 
        'right': right
    }

def compute_distance(left: List[int], right: List[int]) -> int:
    distance = 0
    for l,r in zip(left,right):
        distance += abs(l - r)
    return distance

if __name__ == '__main__':
    inputs = parse_input()
    distance = compute_distance(
        sorted(inputs.get('left')),
        sorted(inputs.get('right'))
    )
    print(
        f'distance is {distance}'
    )