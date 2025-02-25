
from .screen import Screen
from .reels import Reels

class SlotScoreCalculator:
    
    def __init__(self, pay_table=None, raw_reels=None, random_num=None):
        self.odd = 0
        self.reels = Reels(raw_reels)
        self.random_num = random_num
        self.pay_table = pay_table

    def spin_single_reel(self, random_num):
        return [self.reels.raw_reels[(random_num + i) % len(self.reels.raw_reels)] for i in range(3)]

    def calculate(self, bet):
        raw_screen = self.reels.reels_to_screen(self.random_num)
        screen = Screen(raw_screen)
        self.odd = self.pay_table.get_odd(screen)
        return self.odd * bet