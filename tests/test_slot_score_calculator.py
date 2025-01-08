import pytest
from src.slot_score_calculator import SlotScoreCalculator

@pytest.fixture
def slot_score_calculator():
    def _slot_score_calculator(wheels):
        return SlotScoreCalculator(wheels)
    return _slot_score_calculator

def test_lose(slot_score_calculator):
    wheels = [
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['2', '3', '4'],
    ]
    assert slot_score_calculator(wheels).calculate(10) == 0

def test_one_line(slot_score_calculator):
    wheels = [
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '3', '4'],
    ]
    assert slot_score_calculator(wheels).calculate(10) == 100

def test_two_line(slot_score_calculator):
    wheels = [
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '4'],
    ]
    assert slot_score_calculator(wheels).calculate(10) == 400

def test_three_line(slot_score_calculator):
    wheels = [
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
    ]
    assert slot_score_calculator(wheels).calculate(10) == 1000