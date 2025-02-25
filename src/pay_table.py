class PayTable:
    PAYTABLE = {
        0: 0,
        1: 10,
        2: 40,
        3: 100
    }

    def _get_lines(self, screen):
        try:
            same_line = 0
            for column in list(zip(*screen)):
                if len(set(column)) == 1:
                    same_line += 1
            return same_line

        except Exception as error:
            print(error)
            return str(error)

    def get_odd(self, screen):
        try:
            same_line = self._get_lines(screen)
            if same_line not in self.PAYTABLE:
                raise RuntimeError('Unsupported lines')
            return self.PAYTABLE[same_line]

        except Exception as error:
            print(error)
            return str(error)