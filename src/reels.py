import random

class Reels:
    def __init__(self, raw_reels, random_num):
        self.raw_reels = raw_reels
        self.random_num = random_num

    def reels_to_screen(self):
        try:
            screen = []
            for reel in self.raw_reels:
                column = [reel[(self.random_num + i) % len(reel)] for i in range(3)]
                screen.append(column)
            return screen

        except Exception as error:
            print(error)
            return str(error)