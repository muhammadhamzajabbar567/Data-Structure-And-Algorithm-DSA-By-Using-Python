n = 5438
num = n
count = 0
while num > 0:
    count += 1
    num = num // 10
print(count)

# -----------------------------------------------
from math import *

def count_digits(num):
    return int(log10(num)+1)

print(count_digits(5438))

