from unittest import TestCase

from main import process_input


class TestProcessInput(TestCase):
    def test_success_case(self):
        numbers_list = "1,2,6,7"
        target_value = "8"
        input_values = f"{numbers_list} {target_value}"
        numbers, target = process_input(input_values)
        self.assertEqual(numbers, numbers_list.split(","))
        self.assertEqual(target, target_value)
