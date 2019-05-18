import utils

def prime_factorization(base, power):
    factorization = utils.prime_factorization(base)
    for factor in factorization:
        factorization[factor] *= power

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
