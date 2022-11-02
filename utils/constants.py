from utils.int_operations import is_prime
PRIME_NUMBERS_2_TO_4_DIGITS = list(filter(lambda num: is_prime(num), [
    i for i in range(10, 10000)]))
PRIME_NUMBER_2_DIGITS = list(
    filter(lambda x: 10 <= x <= 99, PRIME_NUMBERS_2_TO_4_DIGITS))
PRIME_NUMBER_3_DIGITS = list(
    filter(lambda x: 100 <= x <= 999, PRIME_NUMBERS_2_TO_4_DIGITS))
PRIME_NUMBER_4_DIGITS = list(
    filter(lambda x: 1000 <= x <= 9999, PRIME_NUMBERS_2_TO_4_DIGITS))
