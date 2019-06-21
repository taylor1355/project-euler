# takes logarithmic time by skipping an exponentially increasing number of digits
def nth_digit(n):
    curr = 1
    index = 1 # using 1-indexing
    place = 1
    curr_length = 1
    while n - index >= place*curr_length*9:
        curr += place*9
        index += place*curr_length*9
        place = max(1, place*10)
        curr_length += 1

    curr += (n - index) // curr_length
    sub_index = (n - index) % curr_length
    return int(str(curr)[sub_index])

max_index = 1000000
product = 1
place = 1
while place <= max_index:
    product *= nth_digit(place)
    place *= 10

print('Product:', product)
