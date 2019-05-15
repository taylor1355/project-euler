def prime_factorization(base, power):
    factorization = {}
    factor = 2
    while base > 1:
        if base % factor == 0:
            if factor not in factorization:
                factorization[factor] = 0
            factorization[factor] += power
            base = base // factor
        else:
            factor += 1

    factorization_str = ''
    for factor, power in factorization.items():
        factorization_str += '{}^{},'.format(factor, power)
    return factorization_str

bases = range(2, 101)
powers = range(2, 101)

factorizations = set()
for base in bases:
    for power in powers:
        factorizations.add(prime_factorization(base, power))

print(len(factorizations))
