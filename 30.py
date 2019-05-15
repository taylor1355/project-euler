# 10^6 > 7*9^5 implies numbers of the desired form
# must only have 5 or fewer nonzero digits

upper_bound = 10**6
lower_bound = 10

sum = 0
for num in range(lower_bound, upper_bound):
    digit_sum = 0
    for char in str(num):
        digit_sum += int(char)**5
    if digit_sum == num:
        sum += num

print("The sum of the numbers that can be written as the sum of fifth powers of their digits is", sum)
