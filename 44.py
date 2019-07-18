# difference between nth and (n+1)th pentagonal numbers is 3n+1
# so if two pentagonal numbers whose difference (d) and sum are
# pentagonal, the largest pentagonal number that needs to be
# considered is the (d-1)/3 - 1 = (d-4)/3 pentagonal number

class PentagonalTracker:
    def __init__(self):
        self.pentagonals = []
        self.pentagonal_set = set()

    def is_pentagonal(self, num):
        while len(self.pentagonals) == 0 or num > self.pentagonals[-1]:
            self.generate_next()
        return num in self.pentagonal_set

    def nth_pentagonal(self, n):
        while len(self.pentagonals) == 0 or n > len(self.pentagonals):
            self.generate_next()
        return self.pentagonals[n - 1]

    def iterate_pentagonals(self, upper_bound=None):
        n = 1
        while True:
            if n > len(self.pentagonals):
                self.generate_next()
            yield self.pentagonals[n-1]
            n += 1
            if upper_bound is not None and n >= upper_bound:
                break

    def generate_next(self):
        n = len(self.pentagonals) + 1
        next = n * (3*n - 1) // 2
        self.pentagonals.append(next)
        self.pentagonal_set.add(next)


tracker = PentagonalTracker()
upper_bound = None
min_difference = None
k = 2
while upper_bound is None or k < upper_bound:
    if k % 10000 == 0:
        print('k =', k)
    high_pentagonal = tracker.nth_pentagonal(k)
    for j in range(k - 1, 0, -1):
        low_pentagonal = tracker.nth_pentagonal(j)
        sum = high_pentagonal + low_pentagonal
        difference = high_pentagonal - low_pentagonal
        if min_difference is not None and difference >= min_difference:
            break
        elif tracker.is_pentagonal(sum) and tracker.is_pentagonal(difference):
            if min_difference is None or difference < min_difference:
                upper_bound = (difference - 1) // 3
                min_difference = difference
                print("Found pair ({}, {}), new upper bound {}".format(low_pentagonal, high_pentagonal, upper_bound))
    k += 1

print("Min Difference:", min_difference)
