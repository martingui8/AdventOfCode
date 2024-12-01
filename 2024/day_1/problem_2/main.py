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

def compute_similarity(left: List[int], right: List[int]) -> int:
    similarity = 0
    for l in left:
        similarity += right.count(l) * l
    return similarity

if __name__ == '__main__':
    inputs = parse_input()
    distance = compute_similarity(
        sorted(inputs.get('left')),
        sorted(inputs.get('right'))
    )
    print(
        f'similarity is {distance}'
    )