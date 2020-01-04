import primes
import utils

pc = primes.PrimeCalculator()
max_pandigital = 0

digits = '1'
for n in range(2, 10):
    digits += str(n)
    for permutation in utils.iterate_permutations(digits):
        num = int(permutation)
        if pc.is_prime(num):
            max_pandigital = max(max_pandigital, num)
            print(num)

print('Max Pandigital Prime:', max_pandigital)
