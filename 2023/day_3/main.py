import re
from typing import List
from Number import Number
from Gear import Gear

symbols = r'[^0-9a-zA-Z\.]'
digits = r'(\d+)'
stars = r'(\*)'

if __name__ == '__main__':
    f = open('test_input.txt')
    numbers: List[Number] = []
    schematic: List[str] = []
    gears: List[Number] = []
    for i, line in enumerate(f.readlines()):
        schematic.append(line.strip())
        re_numbers = re.finditer(digits, line.strip())
        for re_number in re_numbers:
            numbers.append(Number(
                row=i,
                start=re_number.start(),
                end=re_number.end(),
                value=re_number.group()
            ))

        re_gears = re.finditer(stars, line.strip())
        for re_gear in re_gears:
            gears.append(Gear(
                row=i,
                column=re_gear.start()
            ))

    part_numbers_sum = 0
    for n in numbers:
        if n.has_neighbours(schematic, symbols):
            part_numbers_sum += n.value

    print(f'Part 1: {part_numbers_sum}')

    gear_ratios_sum = 0
    for gear in gears:
        gear.compute_ratio(numbers)
        gear_ratios_sum += gear.ratio

    print(f'Part 2: {gear_ratios_sum}')