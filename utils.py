

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
