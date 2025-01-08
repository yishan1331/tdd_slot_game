
class SlotScoreCalculator:
    def __init__(self, wheels):
        self.odd = 0
        self.wheels = wheels

    def calculate(self, bet):
        transposed = list(zip(*self.wheels))

        same_line = 0
        for column in transposed:
            if len(set(column)) == 1:
                same_line += 1

        if same_line == 1: self.odd = 10
        return self.odd * bet