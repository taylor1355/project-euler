import math
# want all integer solutions of a+b+c=p (specifying perimeter), a^2+b^2=c^2 (right triangle constraint)
# first parameterize a and b as x=a+b, y=a^2+b^2 giving x=p-c, y=c^2
# solving for a and b in terms of x and y, we get x^2=y+2ab
# which yields a,b = (x + or - sqrt(8y-4x^2)/2) / 2
# since x, y are functions of p and c, and p is given, only c values need to be searched over

max_p = 0
max_num_solutions = 0

for p in range(3, 1001):
    solutions = 0
    for c in range(1, p-1):
        x = p - c
        y = c**2
        radicand = 8*y - 4*x**2
        if radicand > 0:
            root = int(math.sqrt(radicand))
            if root**2 == radicand and root % 2 == 0 and (x + root//2) % 2 == 0: # making sure a, b are integers
                a = (x + root//2) // 2
                b = (x - root//2) // 2
                if min(a, b) > 0:
                    if solutions == 0:
                        print('p =', p)
                    print('({},{},{})'.format(min(a,b), max(a,b), c))
                    solutions += 1

    if solutions > 0:
        print()

    if solutions > max_num_solutions:
        max_p = p
        max_num_solutions = solutions

print('Maximal p={} has {} integer solutions'.format(max_p, max_num_solutions))
