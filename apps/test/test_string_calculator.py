import pytest

from apps.string_calculator.string_calculator import StringCalculator


class TestStringCalculator(object):
    def test_0개_숫자를_numbers_인자로받아_합계를_반환한다(self):
        # arrange
        numbers1 = ''
        numbers2 = ' '
        # act
        result1 = StringCalculator.add(numbers1)
        result2 = StringCalculator.add(numbers2)
        # assert
        assert result1 == 0
        assert result2 == 0

    def test_1개_숫자를_numbers_인자로받아_합계를_반환한다(self):
        # arrange
        numbers = '1'
        # act
        result = StringCalculator.add(numbers)
        # assert
        assert result == 1

    def test_2개_숫자를_numbers_인자로받아_합계를_반환한다(self):
        # arrange
        numbers = '1,2'
        # act
        result = StringCalculator.add(numbers)
        # assert
        assert result == 3

    def test_2개_숫자를_numbers_인자로받아_합계를_반환한다(self):
        # arrange
        numbers = '1,2'
        # act
        result = StringCalculator.add(numbers)
        # assert
        assert result == 3


