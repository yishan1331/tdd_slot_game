
import random

class SlotScoreCalculator:
    PAYTABLE = {
        0: 0,
        1: 10,
        2: 40,
        3: 100
    }
    def __init__(self, reels=None, random_num=None):
        self.odd = 0
        self.reels = reels
        self.random_num = random_num
    
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

    def _get_screen(self):
        try:
            screen = []
            for reel in self.reels:
                column = [reel[(self.random_num + i) % len(reel)] for i in range(3)]
                screen.append(column)
            return screen

        except Exception as error:
            print(error)
            return str(error)

    def spin_single_reel(self, random_num):
        return [self.reels[(random_num + i) % len(self.reels)] for i in range(3)]

    def calculate(self, bet):
        screen = self._get_screen()
        self.odd = self._get_odd(screen)
        return self.odd * bet