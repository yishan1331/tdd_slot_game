class Screen:
    def __init__(self, raw_screen):
        self.raw_screen = raw_screen

    def count_straight_lines(self):
        try:
            same_line = 0
            for column in list(zip(*self.raw_screen)):
                if len(set(column)) == 1:
                    same_line += 1
            return same_line

        except Exception as error:
            print(error)
            return str(error)