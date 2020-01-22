import primes
import utils

pc = primes.PrimeCalculator()

digits = [digit for digit in range(1, 10)]
num_digits = 4
sequence_len = 3

for digit_count in utils.iterate_digit_counts(num_digits, lowest_digit=1):
    digits = utils.digit_counts_to_digits(digit_count)
    primes = []
    for permutation in utils.iterate_permutations(digits):#TODO: not working
        # print(permutation)
        num = utils.digits_to_int(permutation)
        # print(num)
        if pc.is_prime(num):
            primes.append(num)

    if len(primes) >= sequence_len:
        # print(primes)
        for prime_combination in utils.iterate_combinations(primes, sequence_len):
            prime_combination.sort()
            # print(prime_combination)
            arithmetic_sequence = True
            expected_difference = prime_combination[1] - prime_combination[0]
            for i in range(0, sequence_len - 1):
                difference = prime_combination[i + 1] - prime_combination[i]
                if difference != expected_difference:
                    arithmetic_sequence = False
                    break

            if arithmetic_sequence:
                print(prime_combination)
        #print()
