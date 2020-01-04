import primes

def print_consecutive(consecutive):
    print('{} consecutive integers: {}'.format(len(consecutive), consecutive))

pc = primes.PrimeCalculator()
num = 2
consecutive = []
while len(consecutive) < 4:
    factorization = pc.prime_factorization(num)
    if len(factorization) == 4:
        consecutive.append('{} = {}'.format(num, factorization))
    else:
        if len(consecutive) > 2:
            print_consecutive(consecutive)
        consecutive = []
    num += 1

print_consecutive(consecutive)
