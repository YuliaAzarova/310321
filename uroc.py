A = list(map(int, input().split()))
n = len(A)

tmp = 0

for i in range(n):
    if A[i] < A[tmp]:
        tmp = i
