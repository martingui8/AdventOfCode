from typing import List, Dict

def parse_input() -> List[List[int]]:
    reports = []
    with open('input.txt') as f:
        line = f.readline() 
        while line:
            reports.append(list(map(
                lambda level: int(level.strip()),
                line.split()
            )))
            line = f.readline()

    return list(reports)

def is_report_safe(report: List[int]) -> bool:
    direction = 0
    for i in range(len(report) - 1):
        variation = report[i] - report[i + 1]
        if abs(variation) > 3: return False
        if abs(variation) < 1: return False
        if direction != 0 and variation / abs(variation) != direction: return False
        direction =  variation / abs(variation)
    return True

if __name__ == '__main__':
    inputs = parse_input()
    count_safe_reports = sum(
        map(
            is_report_safe,
            inputs
        )
    )
    print(f'There are {count_safe_reports} safe reports')