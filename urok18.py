A = list(map(int, input().split()))
n = len(A)
for i in range(0, n, 2):
    A[i], A[i+1] = A[i+1], A[i]
print(A)