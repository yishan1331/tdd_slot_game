#Design By Contract

from .errors import PreConditionViolatedException

class DBC:
    @staticmethod
    def check_pre_condition(pre_condition, message):
        if pre_condition:
            raise PreConditionViolatedException(message)
