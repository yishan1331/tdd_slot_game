
from .screen import Screen
from .reels import Reels

class SlotScoreCalculator:
    
    def __init__(self, pay_table=None, raw_reels=None, random_num=None):
        self.odd = 0
        self.pay_table = pay_table
        self.reels = Reels(raw_reels, random_num)

    def spin_single_reel(self):
        return [self.reels.raw_reels[(self.reels.random_num + i) % len(self.reels.raw_reels)] for i in range(3)]

    def calculate(self, bet):
        raw_screen = self.reels.reels_to_screen()
        screen = Screen(raw_screen)
        self.odd = self.pay_table.get_odd(screen)
        return self.odd * bet