
class SlotScoreCalculator:
    PAYTABLE = {
        0: 0,
        1: 10,
        2: 40,
        3: 100
    }
    def __init__(self, wheels):
        self.odd = 0
        self.wheels = wheels
    
    def _get_odd(self):
        try:
            transposed = list(zip(*self.wheels))

            same_line = 0
            for column in transposed:
                if len(set(column)) == 1:
                    same_line += 1

            if same_line not in self.PAYTABLE:
                raise RuntimeError('TBD')
            return self.PAYTABLE[same_line]

        except Exception as error:
            print(error)

    def calculate(self, bet):
        self.odd = self._get_odd()
        return self.odd * bet