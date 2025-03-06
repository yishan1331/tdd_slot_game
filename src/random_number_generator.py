class RandomNumberGenerator:
    def __init__(self, random_num=None):
        self.random_num = random_num
    
    def next_random_int(self, bound):
        return