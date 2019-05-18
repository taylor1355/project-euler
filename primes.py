import math
import time

class PrimeCalculator:
    def __init__(self):
        self.primes = [2, 3, 5, 7, 11, 13, 17]
        self.flt_bases = list(self.primes)
        self.coprime_classes, self.modulus = self.coprime_congruence_classes(self.primes)

    def prime_factorization(self, num):
        factorization = {}
        for factor in self.iterate_primes():
            if num <= 1:
                break
            while num % factor == 0:
                if factor not in factorization:
                    factorization[factor] = 0
                factorization[factor] += 1
                num = num // factor
        return factorization

    def iterate_primes(self, start_index=0, upper_bound=None):
        i = start_index
        while True:
            self.expand_if_needed(i)
            if upper_bound is not None and self.primes[i] > upper_bound:
                break
            yield self.primes[i]
            i += 1

    def iterate_factorizations(self, upper_bound):
        for prime_factorization in self.iterate_factorizations_helper(0, upper_bound, {}):
            yield prime_factorization

    def test_time(self):
        for i in range(9):
            upper_bound = int(10**i)
            start_prime = time.time()
            primes = [p for p in self.iterate_primes(upper_bound=upper_bound)]
            print('Upper Bound', upper_bound)
            print('Prime Time:', time.time() - start_prime, 'sec')
            start_iter = time.time()
            arr = [f for f in self.iterate_factorizations(upper_bound)]
            print('Iter Time:', time.time() - start_iter, 'sec')
            start_fact = time.time()
            arr = [self.prime_factorization(n) for n in range(1, upper_bound + 1)]
            print('Fact Time:', time.time() - start_fact, 'sec')
            print()

    def iterate_factorizations_helper(self, start_index, upper_bound, curr_factorization):
        i = 0
        for prime in self.iterate_primes(start_index=start_index, upper_bound=upper_bound):
            new_factorization = curr_factorization.copy()
            if prime not in new_factorization:
                new_factorization[prime] = 0
            new_factorization[prime] += 1
            yield new_factorization

            for factorization in self.iterate_factorizations_helper(i, upper_bound // prime, new_factorization):
                yield factorization

            i += 1

    def expand_if_needed(self, index):
        while index > len(self.primes) - 1:
            self.generate_next_prime()

    def generate_next_prime(self):
        for candidate in self.generate_candidates(start=self.primes[-1]):
            prob = self.probably_prime(candidate)
            # print(candidate, prob, False if not prob else self.is_prime(candidate))
            if self.probably_prime(candidate) and self.is_prime(candidate):
                self.primes.append(candidate)
                break

    # find the set of congruence classes mod product(primes)
    # coprime to each prime in primes (modulus determined by Chinese
    # Remainder Theorem)
    def coprime_congruence_classes(self, primes):
        modulus = self.product(primes)
        coprime_congruence_classes = set([num for num in range(1, modulus)])
        for prime in primes:
            prime_multiple = prime
            while prime_multiple < modulus:
                coprime_congruence_classes.discard(prime_multiple)
                prime_multiple += prime
        coprime_congruence_classes = list(coprime_congruence_classes)
        coprime_congruence_classes.sort()
        return coprime_congruence_classes, modulus

    # use partial Sieve of Eratosthenes to narrow down possibilities
    def generate_candidates(self, start=0): # TODO: use binary search to set initial coprime index
        offset = self.modulus * (start // self.modulus)
        while True:
            for coprime_class in self.coprime_classes:
                if coprime_class + offset > start: # TODO: remove this
                    yield coprime_class + offset
            offset += self.modulus

    # iterate through potential divisors until sqrt(num) is reached with no divisors found
    def is_prime(self, num):
        divisor_bound = int(math.sqrt(num))
        for prime in self.iterate_primes():
            if prime > divisor_bound:
                break

            if num == prime:
                return True
            elif num % prime == 0:
                return False

        return True

    # a number is most likely prime if the converse of FLT holds for
    # several (or even 1) coprime bases
    def probably_prime(self, num):
        for coprime in self.flt_bases:
            if num % coprime == 0 or (coprime < num and not self.flt_converse(coprime, num)):
                return False
        return True

    # returns whether the converse of Fermat's Little Theorem (FLT)
    # holds for prime candidate p and coprime base a
    def flt_converse(self, a, p):
        return self.fast_modular_exponentiation(a, p-1, p) == 1

    def fast_modular_exponentiation(self, base, power, modulus):
        result = 1
        square = base
        while power > 0:
            if power % 2 == 1:
                result = (result * square) % modulus
            power = power >> 1
            square = (square * square) % modulus
        return result

    def product(self, nums):
        curr_product = 1
        for num in nums:
            curr_product *= num
        return curr_product
