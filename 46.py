import utils
import primes

# a number can be written as the sum of a prime and
# twice a perfect square if there is some prime, p:
# p < n, n-p is even, (n-p)/2 is a perfect square

def iterate_odd_composites(prime_calculator):
    num = 9
    while True:
        if not prime_calculator.is_prime(num):
            yield num
        num += 2

pc = primes.PrimeCalculator()

for num in iterate_odd_composites(pc):
    satisfies_conjecture = False

    for prime in pc.iterate_primes(upper_bound=num):
        leftover = num - prime
        if leftover % 2 == 0 and utils.is_perfect_square(leftover // 2):
            satisfies_conjecture = True
            break

    if not satisfies_conjecture:
        print(num, "doesn't satisfy conjecture")
        break
