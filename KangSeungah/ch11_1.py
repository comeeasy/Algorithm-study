n = int(input())

m = list(map(int, input().split()))

m.sort()

member = 0
count = 0

for i in range(n):
    member += 1
    if member >= m[i]:
        count += 1
        member = 0

print(count)


