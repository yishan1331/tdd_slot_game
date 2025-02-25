import random
from .screen import Screen

class Reels:
    def __init__(self, raw_reels, random_num=0):
        self.raw_reels = raw_reels
        self.random_num = random_num
        if isinstance(random_num, int):
            self.random_num = [random_num] * len(self.raw_reels)
        elif isinstance(random_num, list):
            if len(random_num) > len(self.raw_reels):
                self.random_num = random_num[:len(self.raw_reels)]
            else:
                self.random_num = random_num+[0]*(len(self.raw_reels)-len(random_num))

    def reels_to_screen(self):
        raw_screen = []
        for idx, reel in enumerate(self.raw_reels):
            column = [reel[(self.random_num[idx] + i) % len(reel)] for i in range(3)]
            raw_screen.append(column)
        return Screen(raw_screen)
