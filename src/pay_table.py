from .DBC import DBC

class PayTable:
    PAYTABLE = {
        0: 0,
        1: 10,
        2: 40,
        3: 100
    }

    def get_odd(self, screen):
        same_line = screen.count_straight_lines()
        pre_condition = same_line not in self.PAYTABLE
        DBC.check_pre_condition(pre_condition, 'Unsupported lines')
        return self.PAYTABLE[same_line]