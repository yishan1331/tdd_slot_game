class PayTable:
    PAYTABLE = {
        0: 0,
        1: 10,
        2: 40,
        3: 100
    }

    def get_odd(self, screen):
        try:
            same_line = screen.count_straight_lines()
            if same_line not in self.PAYTABLE:
                raise RuntimeError('Unsupported lines')
            return self.PAYTABLE[same_line]

        except Exception as error:
            print(error)
            return str(error)