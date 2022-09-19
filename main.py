import sys
from typing import List, Tuple

from errors import MatchingPairsNotFound, InvalidInputError, InvalidInputValuesError


def process_input(input: str) -> Tuple:
    INPUT_LEN = 2
    input_split = input.split(" ")
    if len(input_split) != INPUT_LEN:
        raise InvalidInputError
    numbers, target_sum = input_split[0], input_split[1]
    numbers = numbers.split(",")
    return numbers, target_sum


def print_output(output_values: set):
    for pair in output_values:
        print(f"+ {pair[0]}, {pair[1]}")


def find_pairs(numbers: List[str], target_sum: str):
    hash_table = dict()
    matching_pairs = set()
    try:
        n = int(target_sum)
        for i in range(len(numbers)):
            num = numbers[i]
            key = str(n - int(num))
            if key in hash_table:
                matching_pairs.add((num, key))
            else:
                hash_table[num] = i
        if not matching_pairs:
            raise MatchingPairsNotFound
    except ValueError:
        raise InvalidInputValuesError
    else:
        return matching_pairs


if __name__ == "__main__":
    args = sys.argv.pop(0)
    input = " ".join(sys.argv)
    numbers, target_sum = process_input(input=input)
    result = find_pairs(numbers, target_sum)
    print_output(result)
