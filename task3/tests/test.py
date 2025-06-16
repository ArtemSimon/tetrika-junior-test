import pytest
from task3.solution import appearance


"""TESTS"""


TEST_CASES = [
    # Test 1: # Проверка простого пересечения интервалов
    (
        {
            'lesson': [100, 200],
            'pupil': [110, 150],
            'tutor': [120, 180]
        },
        30  # Пересечение: [120, 150] -> 30 сек
    ),
    # Test 2:  Проверка при нескольких интервалах у ученика
    (
        {
            'lesson': [100, 200],
            'pupil': [110, 130, 140, 160],
            'tutor': [120, 180]
        },
        30  # Пересечения: [120,130] + [140,160] -> 10 + 20 = 30 сек
    ),
    # Test 3:  Проверка при отсутствии пересечений
    (
        {
            'lesson': [100, 200],
            'pupil': [110, 130],
            'tutor': [140, 180]
        },
        0
    ),
    # Test 4: Проверка при отсутствии интервалов 
    (
        {
            'lesson': [100, 200],
            'pupil': [],
            'tutor': [120, 180]
        },
        0
    ),
    # Test 5: Проверка при полном совпадении интервалов
    (
        {
            'lesson': [100, 200],
            'pupil': [100, 200],
            'tutor': [100, 200]
        },
        100
    ),
    # Test 6: Проверка крайних точек урока
    (
        {
            'lesson': [100, 200],
            'pupil': [100, 150, 150, 200],
            'tutor': [100, 200]
        },
        100
    )
]

@pytest.mark.parametrize("intervals,expected_result", TEST_CASES)
def test_appearance(intervals, expected_result):
    assert appearance(intervals) == expected_result
