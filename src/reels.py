import random

class Reels:
    def __init__(self, raw_reels):
        self.raw_reels = raw_reels

    def reels_to_screen(self, random_num):
        try:
            screen = []
            for reel in self.raw_reels:
                column = [reel[(random_num + i) % len(reel)] for i in range(3)]
                screen.append(column)
            return screen

        except Exception as error:
            print(error)
            return str(error)