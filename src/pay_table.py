from .screen import Screen

class PayTable:
    PAYTABLE = {
        0: 0,
        1: 10,
        2: 40,
        3: 100
    }

    def get_odd(self, raw_screen):
        try:
            same_line = Screen().count_straight_lines(raw_screen)
            if same_line not in self.PAYTABLE:
                raise RuntimeError('Unsupported lines')
            return self.PAYTABLE[same_line]

        except Exception as error:
            print(error)
            return str(error)