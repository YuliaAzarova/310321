a = int(input())
b = int(input())
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    return max(a, b)
print(gcd(a,b))