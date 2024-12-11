from typing import List, Tuple, Dict
import math
import re

def parse_input() -> List[List[int]]:
    roofs = []
    with open('input.txt') as f:
        row = f.readline() 
        while row:
            roofs.append(list(row.strip()))
            row = f.readline()
    return roofs

def list_antennas(input: List[List[int]]) -> List[Dict[str, Tuple[int,int]]]:
    antennas = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if re.match(r'^[0-9a-zA-Z]$', input[i][j]):
                antennas.append(
                    {
                        'value': input[i][j],
                        'coordinates': (i, j)
                    }
                )
    return antennas

def add(v1: Tuple[int,int], v2: Tuple[int,int]) -> Tuple[int,int]:
    return tuple( a + b for a,b in  zip(v1,v2))

def sub(v1: Tuple[int,int], v2: Tuple[int,int]) -> Tuple[int,int]:
    return tuple( a - b for a,b in zip(v1,v2) )

def normalize(v: Tuple[int,int]) -> Tuple[int,int]:
    gcd = math.gcd(v[0], v[1])
    return (v[0] // gcd, v[1] // gcd)

def is_within_bounds(node: Tuple[int, int], bounds: Tuple[int, int]) -> bool:
    if node[0] < 0 or node[1] < 0: return False
    if bounds[0] <= node[0] or bounds[1] <= node[1]: return False
    return True

def compute_anti_nodes(antennaA: Tuple[int,int], antennaB: Tuple[int,int], bounds: Tuple[int, int]) -> List[Tuple[int, int]]:
    anti_nodes = []
    vector = normalize(sub(antennaA, antennaB))
    node = antennaA
    while is_within_bounds(node, bounds):
        anti_nodes.append(node)
        node = add(node, vector)

    node = antennaB
    while is_within_bounds(node, bounds):
        anti_nodes.append(node)
        node = sub(node, vector)

    return anti_nodes

def list_anti_nodes(antennas: List[Dict[str, Tuple[int,int]]], bounds: Tuple[int, int]) -> List[Tuple[int,int]]:
    all_anti_nodes = []
    for a in range(len(antennas) - 1):
        for b in range(a + 1, len(antennas)):
            if antennas[a]['value'] != antennas[b]['value']: continue
            anti_nodes = compute_anti_nodes(antennas[a]['coordinates'], antennas[b]['coordinates'], bounds)
            for node in anti_nodes:
                all_anti_nodes.append(node)
    return all_anti_nodes

def get_shape(map: List[List[int]]) -> Tuple[int,int]:
    return (len(map), len(map[0]))

if __name__ == '__main__':
    input = parse_input()
    bounds = get_shape(input)
    antennas = list_antennas(input)
    all_anti_nodes = set(list_anti_nodes(antennas, bounds))

    for an in all_anti_nodes:
        if input[an[0]][an[1]] == '.':
            input[an[0]][an[1]] = '#'
    print(len(all_anti_nodes))
    with open('output.txt', 'w') as f:
        for row in input:
            f.write(''.join(row) + '\n')