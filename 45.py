import utils

def next_hexagonal(sequence):
    n = len(sequence) + 1
    return utils.nth_hexagonal(n)
hexagonals = utils.Sequence(next_hexagonal)

lower_bound = 40755
for num in hexagonals.iterate():
    if utils.is_triangular(num) and utils.is_pentagonal(num):
        print(num, 'is triangular, pentagonal, and hexagonal')
        if num > lower_bound:
            break
