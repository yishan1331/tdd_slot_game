class Screen:
    def count_straight_lines(self, raw_screen):
        try:
            same_line = 0
            for column in list(zip(*raw_screen)):
                if len(set(column)) == 1:
                    same_line += 1
            return same_line

        except Exception as error:
            print(error)
            return str(error)