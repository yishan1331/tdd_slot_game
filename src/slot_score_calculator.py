
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
    
    def _get_lines(self, screen):
        try:
            same_line = 0
            for column in list(zip(*screen)):
                if len(set(column)) == 1:
                    same_line += 1
            return same_line

        except Exception as error:
            print(error)
            return str(error)

    def _get_odd(self, screen):
        try:
            same_line = self._get_lines(screen)
            if same_line not in self.PAYTABLE:
                raise RuntimeError('Unsupported lines')
            return self.PAYTABLE[same_line]

        except Exception as error:
            print(error)
            return str(error)

    def calculate(self, bet):

        screen = self.wheels

        self.odd = self._get_odd(screen)
        return self.odd * bet