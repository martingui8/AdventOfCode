from typing import List, Dict, Tuple

def parse_rules(input: str) -> List[Tuple[int,int]]:
    rules = []
    for rule in input.split('\n'):
        page1st,_, page2nd = rule.partition('|')
        rules.append((int(page1st), int(page2nd)))
    return rules

def parse_updates(input: str) -> List[int]:
    return [
        [int(u.strip()) for u in update.split(',')]
        for update in input.strip().split('\n')
    ]

def parse_input() -> Tuple[List[Tuple[int,int]], List[int]]:
    with open('input.txt') as f:
        input = f.read()    
    raw_rules, raw_updates = input.split('\n\n')
    return parse_rules(raw_rules), parse_updates(raw_updates)

def is_update_valid(update: List[int], rules: List[Tuple[int,int]]) -> bool:
    update_set = set(update)
    for rule in rules:
        if not rule[0] in update_set: continue
        if not rule[1] in update_set: continue
        if update.index(rule[0]) > update.index(rule[1]): return False
    return True

def make_update_valid(update: List[int], rules: List[Tuple[int,int]]) -> bool:
    update_set = set(update)
    r = 0
    while r < len(rules):
        rule = rules[r]
        if not rule[0] in update_set:
            r += 1
            continue
        if not rule[1] in update_set:
            r += 1
            continue
        index1, index2 = update.index(rule[0]), update.index(rule[1])
        if index1 > index2: 
            update = update[:index2] + update[index2 + 1:index1 + 1] + [update[index2]] + update[index1 + 1:]
            r = 0
        else:
            r += 1
    return update


def get_middle_page_number(update: List[int]) -> int:
    return update[len(update) // 2]

if __name__ == '__main__':
    rules, updates = parse_input()

    result = sum([
        get_middle_page_number(make_update_valid(update, rules))
        for update in updates
        if not is_update_valid(update, rules)
    ])
    print(f'Result is {result}')