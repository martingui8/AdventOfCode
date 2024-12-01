import re
from typing import List
from functools import reduce
from Number import Number


class Gear:
    row: int
    column : int
    ratio: int

    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    def compute_ratio(self, numbers: List[Number]):
        ratio_numbers = []
        for n in numbers:
            if abs(n.row - self.row) <= 1 and (abs(n.start - self.column) <= 1 or abs(n.end - self.column) <= 1):
                ratio_numbers.append(n.value)
        if len(ratio_numbers) != 2:
            self.ratio = 0 
        self.ratio = reduce(lambda acc,n: acc * n, ratio_numbers, 1)
    
