class StringCalculator(object):
    @staticmethod
    def add(numbers):
        strip_numbers = numbers.strip()
        if not strip_numbers:
            return 0

        numbers_list = strip_numbers.split(',')
        result = 0
        for number in numbers_list:
            result += int(number)

        return result
