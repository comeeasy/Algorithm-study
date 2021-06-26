n = int(input())

k = list(map(int, input().split()))

maximum = [0] * 100

maximum[0] = k[0]
maximum[1] = max(maximum[0], k[1])

for i in range(2, n):
    maximum[i] = max(maximum[i-1], k[i] + maximum[i-2])

print(maximum[n-1])
