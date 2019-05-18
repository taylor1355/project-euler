import utils

def is_close(num1, num2):
    return abs(num2 - num1) < 1e-8

digit_canceling_num = 1
digit_canceling_denom = 1
for n in range(10, 100):
    for d in range(n + 1, 100):
        simplified = []
        if n // 10 == d // 10:
            simplified.append((n % 10) / (d % 10))
        if n % 10 == d % 10 and n % 10 != 0:
            simplified.append((n // 10) / (d // 10))
        if n % 10 == d // 10 and d % 10 != 0:
            simplified.append((n // 10) / (d % 10))
        if n // 10 == d % 10:
            simplified.append((n % 10) / (d // 10))
        for frac in simplified:
            print(n, '/', d)
            if is_close(frac, n / d):
                digit_canceling_num *= n
                digit_canceling_denom *= d
                break

print(digit_canceling_num, '/', digit_canceling_denom)

gcd = utils.gcd(digit_canceling_num, digit_canceling_denom)
print(digit_canceling_num // gcd, '/', digit_canceling_denom // gcd)
