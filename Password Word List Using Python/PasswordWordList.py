from string import *
from itertools import product

values = ascii_letters + digits + punctuation

for i in range(1,4):
    for j in product(values, repeat=i):
        words = "".join(j)
        file = open('Passwords.txt', 'a')
        file.write(words)
        file.write("\n")