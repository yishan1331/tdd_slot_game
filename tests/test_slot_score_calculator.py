import pytest
import random
from src.pay_table import PayTable
from src.reels import Reels
from src.screen import Screen
from src.random_number_generator import RandomNumberGenerator
from src.slot_score_calculator import SlotScoreCalculator

@pytest.fixture
def slot_score_calculator():
    def _slot_score_calculator(pay_table=None, reels=None):
        return SlotScoreCalculator(pay_table, reels)
    return _slot_score_calculator

# 定義一個fixture來模擬random.randint
@pytest.fixture
def mock_random(mocker):
    def _set_return_value(value):
        mock = mocker.patch('random.randint', return_value=value)
        return mock.return_value  # 返回設置的值
    return _set_return_value

# 使用fixtures的測試
def test_spin_single_reel(slot_score_calculator, mock_random):
    raw_reels = [
        ['A', '2', '3']
    ]
    # 測試第一個位置
    RNG = RandomNumberGenerator(mock_random(0), raw_reels[0])
    result = slot_score_calculator(reels=Reels(raw_reels[0], RNG)).spin_single_reel()
    assert result == ['A', '2', '3']
    
    # 測試最後一個位置
    RNG = RandomNumberGenerator(mock_random(2), raw_reels[0])
    result = slot_score_calculator(reels=Reels(raw_reels[0], RNG)).spin_single_reel()
    assert result == ['3', 'A', '2']

    # 測試最後一個位置
    RNG = RandomNumberGenerator(mock_random(4), raw_reels[0])
    result = slot_score_calculator(reels=Reels(raw_reels[0], RNG)).spin_single_reel()
    assert result == ['2', '3', 'A']

def test_lose(slot_score_calculator, mock_random):
    raw_reels = [
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
    ]
    RNG = RandomNumberGenerator(mock_random([1,1,1,1,2]), raw_reels)
    spin_result = slot_score_calculator(PayTable(), Reels(raw_reels, RNG)).calculate(10)
    assert spin_result[0] == 0
    assert spin_result[1].raw_screen == Screen([
        ['2', '3', 'A'],
        ['2', '3', 'A'],
        ['2', '3', 'A'],
        ['2', '3', 'A'],
        ['3', 'A', '2'],
    ]).raw_screen

def test_one_line(slot_score_calculator, mock_random):
    raw_reels = [
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '3', '4'],
    ]
    RNG = RandomNumberGenerator(mock_random(1), raw_reels)
    spin_result = slot_score_calculator(PayTable(), Reels(raw_reels, RNG)).calculate(10)
    assert spin_result[0] == 100
    assert spin_result[1].raw_screen == Screen([
        ['2', '3', 'A'],
        ['2', '3', 'A'],
        ['2', '3', 'A'],
        ['2', '3', 'A'],
        ['3', '4', 'A'],
    ]).raw_screen

def test_two_line(slot_score_calculator, mock_random):
    raw_reels = [
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '4'],
    ]
    RNG = RandomNumberGenerator(mock_random(3), raw_reels)
    spin_result = slot_score_calculator(PayTable(), Reels(raw_reels, RNG)).calculate(10)
    assert spin_result[0] == 400
    assert spin_result[1].raw_screen == Screen([
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '4'],
    ]).raw_screen

def test_three_line(slot_score_calculator, mock_random):
    raw_reels = [
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
    ]
    RNG = RandomNumberGenerator(mock_random(0), raw_reels)
    spin_result = slot_score_calculator(PayTable(), Reels(raw_reels, RNG)).calculate(10)
    assert spin_result[0] == 1000
    assert spin_result[1].raw_screen == Screen([
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
    ]).raw_screen