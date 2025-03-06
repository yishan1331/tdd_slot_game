from .screen import Screen
from .random_number_generator import RandomNumberGenerator

class Reels:
    def __init__(self, raw_reels, random_num=None):
        self.raw_reels = raw_reels
        self.random_num = RandomNumberGenerator(random_num, raw_reels).gen_random_list()

    def reels_to_screen(self):
        raw_screen = []
        for idx, reel in enumerate(self.raw_reels):
            column = [reel[(self.random_num[idx] + i) % len(reel)] for i in range(3)]
            raw_screen.append(column)
        return Screen(raw_screen)
