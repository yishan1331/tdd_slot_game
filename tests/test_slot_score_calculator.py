import pytest
import random
from src.pay_table import PayTable
from src.slot_score_calculator import SlotScoreCalculator

@pytest.fixture
def slot_score_calculator():
    def _slot_score_calculator(pay_table=None, raw_reels=None, random_num=None):
        return SlotScoreCalculator(pay_table, raw_reels, random_num)
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
    reels = [
        ['A', '2', '3']
    ]
    # 測試第一個位置
    random_num = mock_random(0)
    result = slot_score_calculator(raw_reels=reels[0]).spin_single_reel(random_num)
    assert result == ['A', '2', '3']
    
    # 測試最後一個位置
    random_num = mock_random(2)
    result = slot_score_calculator(raw_reels=reels[0]).spin_single_reel(random_num)
    assert result == ['3', 'A', '2']

    # 測試最後一個位置
    random_num = mock_random(4)
    result = slot_score_calculator(raw_reels=reels[0]).spin_single_reel(random_num)
    assert result == ['2', '3', 'A']

def test_lose(slot_score_calculator, mock_random):
    reels = [
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['2', '3', '4'],
    ]
    random_num = mock_random(1)
    assert slot_score_calculator(PayTable(), raw_reels=reels, random_num=random_num).calculate(10) == 0

def test_one_line(slot_score_calculator, mock_random):
    reels = [
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '3', '4'],
    ]
    random_num = mock_random(1)
    assert slot_score_calculator(PayTable(), reels, random_num).calculate(10) == 100

def test_two_line(slot_score_calculator, mock_random):
    reels = [
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '4'],
    ]
    random_num = mock_random(3)
    assert slot_score_calculator(PayTable(), reels, random_num).calculate(10) == 400

def test_three_line(slot_score_calculator, mock_random):
    reels = [
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
        ['A', '2', '3'],
    ]
    random_num = mock_random(0)
    assert slot_score_calculator(PayTable(), reels, random_num).calculate(10) == 1000