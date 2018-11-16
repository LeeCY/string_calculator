class StringCalculator(object):
    @staticmethod
    def add(numbers):
        strip_numbers = numbers.strip()
        if not strip_numbers:
            return 0

        numbers_list = strip_numbers.split(',')
        result = 0
        for number in numbers_list:
            if number:
                new_line_number_list = number.split('\n')
                for new_line_number in new_line_number_list:
                    result += int(new_line_number)

        return result
