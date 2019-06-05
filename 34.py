import utils

# upper bound is where 10^k > (k+1)*9!, achieved for k=7
# iterate through all possible digit counts for 8 digits,
# determining if each digit count corresponds to a number of
# the desired form

def facorial_digit_sum(digit_counts):
    factorial = 1
    sum = 0
    for i in range(len(digit_counts)):
        if i > 0:
            factorial *= i
        sum += digit_counts[i] * factorial
    return sum

# assumes num < 10^(num_digits+1)
def matches_count(num, count, num_digits):
    count_copy = list(count)
    for digit in str(num): # check for mismatches
        index = int(digit)
        count_copy[index] -= 1

    if len(str(num)) < num_digits: # add trailing 0's
        count_copy[0] -= num_digits - len(str(num))

    for index in range(len(count_copy)): # check for omissions
        if count_copy[index] != 0:
            return False

    return True

nums = 0
sum = 0
digits = 8
for possibility in utils.iterate_digit_counts(digits):
    factorial_sum = facorial_digit_sum(possibility)
    for num_trailing_zeros in range(possibility[0] + 1): # trailing zeros not counted for factorial digit sum
        nums += 1
        curr_factorial_sum = factorial_sum - num_trailing_zeros
        if matches_count(curr_factorial_sum, possibility, digits) and 1 < len(str(curr_factorial_sum)) == digits - num_trailing_zeros and len(str(curr_factorial_sum)):
            sum += curr_factorial_sum
            print(curr_factorial_sum)
            print(possibility)
            print()

print(nums, 'numbers examined (from 0 to', str(int(10**(digits-1))) + ')')
print('sum is ', sum)
