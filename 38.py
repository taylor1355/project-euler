
# largest multiplier that can be considered is 9999, as the concatenated product of 10000 and (1,2) is more than 9 digits
# for each multiplier, multiply by successively higher natural numbers starting at 1 until the concatenated product is 9 digits
# stop at any point if a duplicate digit is produced

upper_bound = 10000
max_concat_prod = 0

for n in range(1, upper_bound):
    digits = set()
    concat_prod = ''
    multiplier = 1
    valid = True # valid if no duplicates and no zeros
    while len(concat_prod) < 9 and valid:
        product = n * multiplier
        for digit in str(product):
            if digit == '0' or digit in digits:
                valid = False
                break
            digits.add(digit)
        concat_prod += str(product)
        multiplier += 1

    if valid and len(concat_prod) == 9:
        debug_out = str(n) + ':'
        for m in range(1, multiplier):
            debug_out += ' ' + str(n * m)
        debug_out += ' ' + str(int(concat_prod))
        print(debug_out)
        max_concat_prod = max(max_concat_prod, int(concat_prod))

print('Max Concat Prod:', max_concat_prod)
