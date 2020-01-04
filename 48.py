import utils

# only needing last 10 digits means performing calculations mod 10^10

modulus = 10**10
max_base = 1000
sum = 0
for base in range(1, max_base + 1):
    power = utils.fast_modular_exponentiation(base, base, modulus)
    sum = (sum + power) % modulus
    print('Sum:', sum)
