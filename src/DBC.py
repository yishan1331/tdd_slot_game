#Design By Contract

class DBC:
    @staticmethod
    def check_pre_condition(pre_condition, message):
        if pre_condition:
            raise RuntimeError(message)
