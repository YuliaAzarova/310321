from time import *
from math import gcd

start = time()
ans = 0
for x in range(100000, 1000000):
    d = gcd(92, x)
    if d == 1:
        ans += 1
print(ans, time() - start)