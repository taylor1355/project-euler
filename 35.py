import primes

def iterate_rotations(num):
    num_str = str(num)
    yield int(num_str)
    for i in range(len(num_str) - 1):
        num_str = num_str[-1] + num_str[:-1]
        yield int(num_str)

pc = primes.PrimeCalculator()

upper_bound = 1000000
count = 0
for prime in pc.iterate_primes(upper_bound=upper_bound-1):
    circular_prime = True
    for rotation in iterate_rotations(prime):
        if not pc.is_prime(rotation):
            circular_prime = False
    if circular_prime:
        print(prime)
        count += 1
print(count, 'circular primes')
