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

    def test_2개_이상의_숫자를_numbers_인자로받아_합계를_반환한다(self):
        # arrange
        numbers = '1,2,3,4,5'
        # act
        result = StringCalculator.add(numbers)
        # assert
        assert result == 15

    def test_numbers에_구분자_사이에_값이_없어도_정상적으로_합계를_반환한다(self):
        # arrange
        numbers = '1,2,3,,4,5'
        # act
        result = StringCalculator.add(numbers)
        # assert
        assert result == 15

    def test_numbers의_구분자로_개행을_사용해도_정상적으로_합계를_반환한다(self):
        # arrange
        numbers = '1\n2\n3'
        # act
        result = StringCalculator.add(numbers)
        # assert
        assert result == 6

    def test_numbers의_구분자로_개행과_콤마를_모두_사용해도_정상적으로_합계를_반환한다(self):
        # arrange
        numbers = '1\n2\n3,4\n5'
        # act
        result = StringCalculator.add(numbers)
        # assert
        assert result == 15

    def test_numbers가_구분자만_가지고_있는경우_0을_반환합니다(self):
        # arrange
        numbers = '\n\n,,\n'
        # act
        result = StringCalculator.add(numbers)
        # assert
        assert result == 0
