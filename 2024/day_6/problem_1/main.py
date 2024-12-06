from typing import List, Tuple, Union

guard_directions_vectors_map = {
    '^': (-1,  0 ),
    '>': ( 0,  1 ),
    'v': ( 1,  0 ),
    '<': ( 0, -1 )
}

guard_directions_list = list(guard_directions_vectors_map.keys())

def parse_input() -> List[List[int]]:
    with open('input.txt') as f:
        input = f.read()    
    rows = input.strip().split('\n')
    return [
        [ cell for cell in row ] 
        for row in rows
    ]

def find_guard(room: List[List[int]]) -> Union[Tuple[int, int], None]:
    for row in range(len(room)):
        for column in range(len(room[row])):
            if room[row][column] in guard_directions_vectors_map: return (row, column)
    return None

def check_location_out_of_bounds(room: List[List[int]], guard_location: Tuple[int, int]) -> bool:
    if guard_location[0] < 0 or guard_location[0] >= len(room): return True
    if guard_location[1] < 0 or guard_location[1] >= len(room[guard_location[0]]): return True
    return False

def run_step(room: List[List[int]], guard_location: Tuple[int, int]) -> Tuple[List[List[int]], Union[Tuple[int, int], None]]:
    guard = room[guard_location[0]][guard_location[1]]
    guard_vector = guard_directions_vectors_map[guard]
    guard_direction_index = guard_directions_list.index(guard)

    next_guard_location = (guard_location[0] + guard_vector[0], guard_location[1] + guard_vector[1])

    if check_location_out_of_bounds(room, next_guard_location):
        return room, None

    if room[next_guard_location[0]][next_guard_location[1]] == '#':
        guard_direction_index = (guard_direction_index + 1) % len(guard_directions_list)
        guard = guard_directions_list[guard_direction_index]
        room[guard_location[0]][guard_location[1]] = guard
        return room, guard_location

    room[guard_location[0]][guard_location[1]] = 'x'
    room[next_guard_location[0]][next_guard_location[1]] = guard
    return room, next_guard_location
    

if __name__ == '__main__':
    room = parse_input()
    guard_location = find_guard(room)
    visited_locations = set()
    if guard_location is None: raise Exception('Guard not found')
    # Uncomment the snippet below to print the evolution of the map at each iteration
    # (use only for smaller size inputs)
    # -------------------------------------------------------------------------------
    # print('Start')
    # for row in room:
    #     print(*row)
    # i = 0
    while True:
        visited_locations.add(str(guard_location))
        room, guard_location = run_step(room, guard_location)
        if guard_location is None: break
        # Uncomment the snippet below to print the evolution of the map at each iteration
        # (use only for smaller size inputs)
        # -------------------------------------------------------------------------------
        # print('---------------------')
        # print(f'Iteration {i}')
        # print(f'The guard visited {len(visited_locations)} locations so far')
        # for row in room:
        #     print(*row)
        # i += 1
    print(f'The guard visited {len(visited_locations)} locations')