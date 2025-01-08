import pytest
from src.slot_score_calculator import SlotScoreCalculator

@pytest.fixture
def slot_score_calculator():
    return SlotScoreCalculator()

def test_lose(slot_score_calculator):
    assert slot_score_calculator.calculate() == 0