class Round:
    blue: int
    green: int
    red: int

    def __init__(self, b: int, g: int, r: int):
        self.blue = b
        self.green = g
        self.red = r

    @classmethod
    def from_string(cls, rawRound: str):
        records = {
            'blue': 0,
            'green': 0,
            'red': 0
        }
        for entry in rawRound.split(','):
            count, _, colour = entry.strip().partition(' ')
            records[colour] = count
        return cls(
            int(records['blue']),
            int(records['green']),
            int(records['red'])
        )

    def __repr__(self) -> str:
        return f'blue: {self.blue} - green: {self.green} - red: {self.red}'
    
    def get_power(self) -> int:
        return self.blue * self.green * self.red