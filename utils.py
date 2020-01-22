import collections
import math

class Sequence:
    def __init__(self, next_func):
        self.next_func = next_func
        self.sequence = []
        self.elements = set()

    def belongs(self, num):
        while len(self.sequence) == 0 or num > self.sequence[-1]:
            self.generate_next()
        return num in self.elements

    # indexed starting at 1
    def nth_element(self, n):
        while len(self.sequence) == 0 or n > len(self.sequence):
            self.generate_next()
        return self.sequence[n - 1]

    def iterate(self, upper_bound=None):
        n = 1
        while True:
            if n > len(self.sequence):
                self.generate_next()
            yield self.sequence[n-1]
            n += 1
            if upper_bound is not None and n >= upper_bound:
                break

    def generate_next(self):
        next = self.next_func(self.sequence)
        self.sequence.append(next)
        self.elements.add(next)

class Counts(collections.UserDict):
    def __init__(self, iterable):
        counts = {}
        if isinstance(iterable, collections.Mapping):
            counts = iterable
        else:
            for element in iterable:
                if element not in counts:
                    counts[element] = 0
                counts[element] += 1

        self.sum = 0
        super().__init__(counts)

    def __delitem__(self, key):
        count = self[key]
        self.sum -= count
        super().__delitem__(key)

    def __setitem__(self, key, count):
        if key in self:
            self.sum -= self[key]
        self.sum += count
        super().__setitem__(key, count)

# iterates through all digit permutations where order doesn't matter and repeats are allowed
def iterate_digit_counts(num_digits, counts=None, lowest_digit=0):
    if counts is None:
        counts = [0] * 10

    if num_digits == 0:
        yield counts
    else:
        for i in range(lowest_digit, len(counts)):
            counts[i] += 1
            for counts in iterate_digit_counts(num_digits - 1, counts, i):
                yield counts
            counts[i] -= 1

# TODO: make a counts class
def digit_counts_to_digits(digit_counts):
    digits = []
    for i in range(len(digit_counts)):
        digits += [i] * digit_counts[i]
    return digits

# iterates through all permutations of a set of elements (with duplicates allowed)
def iterate_permutations(elements, num_to_permute=None):
    counts = Counts(elements)

    if num_to_permute is None:
        num_to_permute = counts.sum

    yield from iterate_permutations_helper(counts, num_to_permute)

def iterate_permutations_helper(counts, num_to_permute):
    if counts.sum == 0 or num_to_permute == 0:
        yield []
        return

    for element in counts.keys():
        if counts[element] > 0:
            counts[element] -= 1
            for sub_permutation in iterate_permutations_helper(counts, num_to_permute - 1):
                yield [element] + sub_permutation
            counts[element] += 1

# iterates through all combinations of a set of elements (with duplicates allowed)
def iterate_combinations(elements, num_to_choose):
    counts = Counts(elements)
    yield from iterate_combinations_helper(counts, num_to_choose)

def iterate_combinations_helper(counts, num_to_choose):
    if counts.sum < num_to_choose or num_to_choose == 0:
        yield []
        return

    element, count = counts.popitem()
    min_sub_count = max(0, num_to_choose - counts.sum)
    max_sub_count = min(num_to_choose, count)
    for sub_count in range(min_sub_count, max_sub_count + 1):
        for sub_combination in iterate_combinations_helper(counts, num_to_choose - sub_count):
            yield [element] * sub_count + sub_combination
    counts[element] = count

def digits_to_int(digits):
    num_str = ''
    for digit in digits:
        num_str += str(digit)
    return int(num_str)

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

def nth_triangular(n):
    return n * (n + 1) // 2

# uses same method described in is_triangular
def is_pentagonal(num):
    radicand = 1 + 24*num
    if radicand > 0 and is_perfect_square(radicand):
        numerator = int(math.sqrt(radicand)) + 1
        return numerator % 6 == 0
    return False

def nth_pentagonal(n):
    return n * (3*n - 1) // 2

# uses same method described in is_triangular
def is_hexagonal(num):
    radicand = 1 + 8*num
    if radicand > 0 and is_perfect_square(radicand):
        numerator = int(math.sqrt(radicand)) + 1
        return numerator % 4 == 0
    return False

def nth_hexagonal(n):
    return n * (2*n - 1)


def is_palindrome(string):
    for i in range((len(string) + 1) // 2):
        if string[i] != string[-1 - i]:
            return False
    return True

def is_perfect_square(num):
    root = int(round(math.sqrt(num)))
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

def fast_modular_exponentiation(base, power, modulus):
    result = 1
    square = base
    while power > 0:
        if power % 2 == 1:
            result = (result * square) % modulus
        power = power >> 1
        square = (square * square) % modulus
    return result

def product(nums):
    curr_product = 1
    for num in nums:
        curr_product *= num
    return curr_product
