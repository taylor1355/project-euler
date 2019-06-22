import math

# iterates through all digit permutations where order doesn't matter
def iterate_digit_counts(num_digits, counts=None, start_index=0):
    if counts is None:
        counts = [0] * 10

    if num_digits == 0:
        yield counts
    else:
        for i in range(start_index, len(counts)):
            counts[i] += 1
            for counts in iterate_digit_counts(num_digits - 1, counts, i):
                yield counts
            counts[i] -= 1

# iterates through all permutations of a string
def iterate_permutations(characters):
    if characters == '':
        yield ''

    for index in range(len(characters)):
        new_characters = characters[:index] + characters[index+1:]
        for sub_permutation in iterate_permutations(new_characters):
            yield characters[index] + sub_permutation

# gcd(a, b) = gcd(b, a-b)
def gcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)

    while b > 1:
        a = max(b, a - b)
        b = min(b, a - b)

    if b == 0:
        return a
    elif b == 1:
        return 1

# can determine if a number is triangular by solving for x=n(n+1)/2
# if the resultant n is a positive integer, then x is triangular
# solving for n gives n = (sqrt(1+8x)-1)/2
def is_triangular(num):
    radicand = 1 + 8*num
    if radicand > 0 and is_perfect_square(radicand):
        numerator = int(math.sqrt(radicand)) - 1
        return numerator > 0 and numerator % 2 == 0
    return False

def is_palindrome(string):
    for i in range((len(string) + 1) // 2):
        if string[i] != string[-1 - i]:
            return False
    return True

def is_perfect_square(num):
    root = int(math.sqrt(num))
    return num == root**2

def to_base(num, base):
    if base > 36:
        raise ValueError('Maximum base is 36')
    base_str = ''
    while num > 0:
        remainder = num % base
        if remainder > 9:
            remainder = chr(ord('a') + remainder - 10)
        base_str = str(remainder) + base_str
        num = num // base
    return base_str
