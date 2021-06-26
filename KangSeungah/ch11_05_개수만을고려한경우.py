n, m = map(int, input().split())
k = list(map(int, input().split()))

# 볼링공 무게에 따른 공의 개수
count = [0] * (m+1)
result = 0

for i in k:
    count[i] += 1

# 8 5
# 1 5 4 3 2 4 5 2
# count : [0, 1, 2, 1, 2, 2]

# A가 고른 공의 무게 => count[i]
# B가 고를 수 있는 공 == (총 볼링공 개수) - (A가 고른 무게의 공의 개수)
# 결과 : (A가 고른 무게의 공의 개수) * (B가 고를 수 있는 공의 개수)
# 공은 모두 다른 공이라는 전제가 있고
# 조합이기 때문에 A,B = (1,2)인것과 (2,1)인것을 구별하지 않음

for i in range(1, m+1):
    n -= count[i]
    result += count[i] * n

print(result)