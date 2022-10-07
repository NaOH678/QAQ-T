import math
import random

s = 2
c = 0
n = 100000
for i in range(n):
    x = random.uniform(0, 1.0)
    y = random.uniform(0, 2.0)
    if y <= x ** 3 + x ** 2:
        c += 1
I = c / n * s

print(I)
