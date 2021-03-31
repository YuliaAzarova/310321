import sys
sys.setrecursionlimit(10**9)

def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)# рекуррентное соотношение

print(f(10 ** 4))