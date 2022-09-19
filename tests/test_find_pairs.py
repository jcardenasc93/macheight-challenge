from unittest import TestCase
from unittest.mock import patch

from main import find_pairs
from errors import MatchingPairsNotFound, InvalidInputValuesError


class TestFindPairs(TestCase):
    def test_success_case(self):
        input_values = ("1,2,6,7".split(","), "8")
        result = find_pairs(numbers=input_values[0], target_sum=input_values[1])
        self.assertSetEqual({("7", "1"), ("6", "2")}, result)

    def test_success_negative_target_sum(self):
        input_values = ("1,2,-6,7".split(","), "-4")
        result = find_pairs(numbers=input_values[0], target_sum=input_values[1])
        self.assertSetEqual({("-6", "2")}, result)

    def test_fail_one_number_list(self):
        input_values = ("1".split(","), "1")
        self.assertRaises(
            MatchingPairsNotFound, find_pairs, input_values[0], input_values[1]
        )

    def test_fail_no_pairs_found(self):
        input_values = ("1,5,10".split(","), "12")
        self.assertRaises(
            MatchingPairsNotFound, find_pairs, input_values[0], input_values[1]
        )

    def test_fail_invalid_input_values(self):
        input_values = ("1,5,aa".split(","), "12")
        self.assertRaises(
            InvalidInputValuesError, find_pairs, input_values[0], input_values[1]
        )
