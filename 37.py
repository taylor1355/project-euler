import primes

pc = primes.PrimeCalculator()
sum = 0
num_truncatable = 0

# could do this more intelligently using a tree structure to construct left truncatable primes from other left truncatable primes and vice versa
for prime in pc.iterate_primes():
    if prime < 10:
        continue
    prime_str = str(prime)
    truncatable = True
    for i in range(1, len(prime_str)):
        left_truncated = int(prime_str[i:])
        right_truncated = int(prime_str[:len(prime_str)-i])
        if not pc.is_prime(left_truncated) or not pc.is_prime(right_truncated):
            truncatable = False
            break
    if truncatable:
        print(prime)
        sum += prime
        num_truncatable += 1
    if num_truncatable == 11:
        break

print('Sum:', sum)
