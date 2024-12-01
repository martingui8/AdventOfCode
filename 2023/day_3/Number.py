import re
from typing import List

class Number:
    row: int
    start: int
    end: int
    value: int

    def __init__(self, row: int, start: int, end: int, value: str):
        self.row = row
        self.start = start
        self.end = end
        self.value = int(value)

    def has_neighbours(self, schematic: List[str], symbols: str):
        for r in schematic[max(0, self.row - 1) : min(len(schematic), self.row + 2)]:
            if re.search(
                symbols,
                r[max(0, self.start - 1) : min(len(r), self.end + 1)]
            ):
                return True
        return False