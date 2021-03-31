A = list(map(int, input().split()))
n = []
for i in range(len(A)):
    if A[i] < 0 or A[i] == 0:
        n += 1
        print(n)