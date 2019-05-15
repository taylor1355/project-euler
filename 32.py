min_digits = 4
max_digits = 5

def iterate_possibilities(num_digits, digits):
    for digit in digits:
        if num_digits > 1:
            for possibility in iterate_possibilities(num_digits - 1, digits - {digit}):
                yield str(digit) + possibility
        else:
            yield str(digit)

pandigital_products = set()

# assume WLOG a <= b
for a_digits in range(1, max_digits // 2 + 1):
    for b_digits in range(min_digits - a_digits, max_digits - a_digits + 1):
        if a_digits <= b_digits:
            print('a, b =', a_digits, b_digits)
            for permutation in iterate_possibilities(a_digits + b_digits, {1, 2, 3, 4, 5, 6, 7, 8, 9}):
                a = int(permutation[:a_digits])
                b = int(permutation[a_digits:])
                product = a * b
                digits = set(permutation).union(set(str(product))) - {'0'}
                if len(str(product)) + a_digits + b_digits == len(digits) == 9:
                    pandigital_products.add(product)
                    print('a*b=p', a, b, product)

sum = 0
for product in pandigital_products:
    sum += product

print('Sum of pandigital products is', sum)
