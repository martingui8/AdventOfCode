import re
from typing import List

class Card:
    id: int
    winning_numbers: List[int]
    card_numbers: List[int]

    def __init__(self, raw: str):
        raw_id, _, raw_card = raw.partition(':')
        self.id = int(
            re.fullmatch(r'Card\s*(\d+)', raw_id)
              .groups()[0]
        )
        raw_winning_numbers, _, raw_card_numbers = raw_card.partition('|')
        self.winning_numbers = [int(n.strip()) for n in raw_winning_numbers.split()]
        self.card_numbers = [int(n.strip()) for n in raw_card_numbers.split()]

    def __repr__(self):
        return f'{self.id}::{self.winning_numbers}||{self.card_numbers}'
    
    def compute_value(self):
        vp = len(self.card_numbers) + len(self.winning_numbers) - len(set(self.card_numbers + self.winning_numbers))
        if vp == 0: return 0
        return 2**(vp-1)