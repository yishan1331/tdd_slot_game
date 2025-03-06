import random
class RandomNumberGenerator:
    def __init__(self, random_num, raw_reels):
        self.random_num = random_num

        bound = len(raw_reels)
        if random_num is None:
            self.random_num = [self._next_random_int(bound - 1) for _ in range(bound)]
        else:
            if isinstance(random_num, int):
                self.random_num = [random_num] * bound
            elif isinstance(random_num, list):
                if len(random_num) > bound:
                    self.random_num = random_num[:bound]
                elif len(random_num) < bound:
                    self.random_num = random_num+[self._next_random_int(bound - 1)]*(bound-len(random_num))

    def _next_random_int(self, bound):
        return random.randint(0, bound)        