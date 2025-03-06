class SlotScoreCalculator:
    
    def __init__(self, pay_table=None, reels=None):
        self.odd = 0
        self.pay_table = pay_table
        self.reels = reels

    def spin_single_reel(self):
        return [self.reels.raw_reels[(self.reels.random_num[0] + i) % len(self.reels.raw_reels)] for i in range(3)]

    def calculate(self, bet):
        try:
            screen = self.reels.reels_to_screen()
            self.odd = self.pay_table.get_odd(screen)
            win = self.odd * bet
            return win, screen
        except Exception as error:
            print(error)
            return str(error)