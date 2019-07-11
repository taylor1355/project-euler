# builds pandigital numbers whose length three substrings
# (from left to right, excluding the first) are divisible,
# respectively, by a sequence of divisors

def build_pandigital(divisors, digits_left, curr=None):
    # print(curr, digits_left)
    if curr is None:
        curr = ''
    elif len(curr) == 10:
        yield curr

    for digit in sorted(list(digits_left)):
        valid = True
        curr += digit
        if len(curr) >= 4: # enforce substring divisibility
            substring = curr[-3:]
            index = len(curr) - 4
            if int(substring) % divisors[index] != 0:
                valid = False
                # print(curr, substring, 'not divisible by', divisors[index])

        digits_left.remove(digit)
        if valid:
            for pandigital in build_pandigital(divisors, digits_left, curr):
                yield pandigital

        digits_left.add(digit)
        curr = curr[:-1]


divisors = [2, 3, 5, 7, 11, 13, 17]
digits_left = set([str(num) for num in range(10)])
sum = 0
for pandigital in build_pandigital(divisors, digits_left):
    print(pandigital)
    sum += int(pandigital)
print('Sum:', sum)
