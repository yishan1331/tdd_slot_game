import pytest
from src.slot_score_calculator import SlotScoreCalculator

@pytest.fixture
def slot_score_calculator():
    def _slot_score_calculator(wheels):
        return SlotScoreCalculator(wheels)
    return _slot_score_calculator

def test_lose(slot_score_calculator):
    wheels = [
        ['A', '1', '2'],
        ['A', '1', '2'],
        ['A', '1', '2'],
        ['A', '1', '2'],
        ['1', '2', '3'],
    ]
    assert slot_score_calculator(wheels).calculate(10) == 0

def test_one_line(slot_score_calculator):
    wheels = [
        ['A', '1', '2'],
        ['A', '1', '2'],
        ['A', '1', '2'],
        ['A', '1', '2'],
        ['A', '2', '3'],
    ]
    assert slot_score_calculator(wheels).calculate(10) == 400