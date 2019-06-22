import utils

def word_value(word):
    value = 0
    for letter in word.upper():
        value += ord(letter) - ord('A') + 1
    return value

count = 0
words_path = 'resources/p042_words.txt'
with open(words_path, 'r') as file:
    for line in file:
        for block in line.split(','):
            word = block[1:-1]
            value = word_value(word)
            if utils.is_triangular(value):
                count += 1
                print(word, value)

print(count, 'triangular words')
