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

def find_pairs(numbers: List[str], target_sum: str):
    hash_table = dict()
    found = False
    try:
        n = int(target_sum)
        for i in range(len(numbers)):
            num = numbers[i]
            key = str(n - int(num))
            if key in hash_table:
                found = True
                print(f"+ {num}, {key}")
            else:
                hash_table[num] = i
        if found is False:
            raise MatchingPairsNotFound
    except ValueError:
        raise InvalidInputValuesError

if __name__ == "__main__":
    input = input("Enter a comma separated list and a target sum value\n")
    numbers, target_sum = process_input(input=input)
    find_pairs(numbers, target_sum)
