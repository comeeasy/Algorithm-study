N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

for i in range(K):
    A[i], B[N-i-1] = B[N-i-1], A[i]

sumA = 0
for j in range(N):
    sumA += A[j]

print(sumA)


