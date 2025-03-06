import random
from .screen import Screen
from .random_number_generator import RandomNumberGenerator

class Reels:
    def __init__(self, raw_reels, random_num=None):
        self.raw_reels = raw_reels
        self.random_num = random_num
        RNG = RandomNumberGenerator()
        if random_num is None:
            self.random_num = [random.randint(0, RNG.next_random_int(len(self.raw_reels) - 1)) for _ in raw_reels]
        else:
            if isinstance(random_num, int):
                self.random_num = [random_num] * len(self.raw_reels)
            elif isinstance(random_num, list):
                if len(random_num) > len(self.raw_reels):
                    self.random_num = random_num[:len(self.raw_reels)]
                elif len(random_num) < len(self.raw_reels):
                    self.random_num = random_num+[random.randint(0, len(self.raw_reels) - 1)]*(len(self.raw_reels)-len(random_num))

    def reels_to_screen(self):
        raw_screen = []
        for idx, reel in enumerate(self.raw_reels):
            column = [reel[(self.random_num[idx] + i) % len(reel)] for i in range(3)]
            raw_screen.append(column)
        return Screen(raw_screen)
