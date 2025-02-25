
import random
from .pay_table import PayTable
from .screen import Screen

class SlotScoreCalculator:
    def __init__(self, reels=None, random_num=None):
        self.odd = 0
        self.reels = reels
        self.random_num = random_num
        self.pay_table = PayTable()

    def _get_raw_screen(self):
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
        raw_screen = self._get_raw_screen()
        screen = Screen(raw_screen)
        self.odd = self.pay_table.get_odd(screen)
        return self.odd * bet