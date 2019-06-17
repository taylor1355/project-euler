import utils

upper_bound = int(10**6)
sum = 0

for i in range(upper_bound):
    base10 = str(i)
    if utils.is_palindrome(base10):
        base2 = utils.to_base(i, 2)
        if utils.is_palindrome(base2):
            sum += i
            print(i)
print('Sum:', sum)
