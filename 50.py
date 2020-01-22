import primes

def find_longest_prime_sum():
    pc = primes.PrimeCalculator()

    # map from (start prime index, number of sum terms) -> sum
    sums = {}

    prime_upper_bound = int(1e6)
    print('Calculating primes...')
    max_index = pc.find_first(lambda prime: prime >= prime_upper_bound) - 1
    print('Finished calculating primes.')

    sums[0, max_index + 1] = sum(pc.iterate_primes(upper_bound=prime_upper_bound))
    for sum_length in reversed(range(1, max_index + 1)):
        for prime_index in range(max_index + 2 - sum_length):
            # reusing effort of previous sums to make each entry of sums doable in O(1)
            if prime_index == 0:
                sums[prime_index, sum_length] = sums[prime_index, sum_length + 1] - pc[prime_index + sum_length]
            else:
                sums[prime_index, sum_length] = sums[prime_index - 1, sum_length] - pc[prime_index - 1] + pc[prime_index + sum_length - 1]

            if sums[prime_index, sum_length] > prime_upper_bound:
                break
            elif pc.is_prime(sums[prime_index, sum_length]):
                print(sums[prime_index, sum_length])
                return

find_longest_prime_sum()
