from typing import List
from Round import Round

class Game:
    id: int
    rounds: List[Round]
    
    def __init__(self, line:str):
        rawId, _, rawRounds = line.partition(':')
        self.id = int(rawId.partition(' ')[2])
        self.rounds = [Round.from_string(r) for r in rawRounds.strip().split(';')]

    def __repr__(self) -> str:
        return f'<Game object id:{self.id} - # rounds: {len(self.rounds)}>'
    
    def reduce(self) -> Round:
        maxRound = Round(0, 0, 0)
        for g in self.rounds:
            if g.blue > maxRound.blue:
                maxRound.blue = g.blue
            if g.green > maxRound.green:
                maxRound.green = g.green
            if g.red > maxRound.red:
                maxRound.red = g.red
        return maxRound

    def is_possible_with_bag(self, blues: int, greens: int, reds: int) -> bool:
        maxRound = self.reduce()
        if blues < maxRound.blue:
            return False
        if greens < maxRound.green:
            return False
        if reds < maxRound.red:
            return False
        return True
    
    def get_power(self):
        return self.reduce().get_power()