INF = int(1e9)

n, m = map(int, input().split())

# graph 의 원소의 값을 무한으로 초기화 (0,0)은 제외하기 때문에 1~n까지를 고려하여 n+1을 해준다.
graph = [[INF] * (n+1) for _ in range(n+1)]

# graph 에서 같은 노드 간의 비용은 0이다.
# 이 문제에서는 하지 않아도 되는 것 같음.
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] == 0


# 직통으로 갈 수 있는 도로가 존재하는 두 회사쌍 (a,b)를 존재하는 경로의 수(m)만큼 입력 받고
# 해당되는 경로에 걸리는 시간 1을 입력해주는데
# 이때 graph는 대칭 행렬이므로 graph[a][b] = 1이면 graph[b][a]도 1이다.
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 출발회사 번호(1) 중간에 거쳐가는 회사번호(k) 최종 도착 회사(x)
x, k = map(int, input().split())


# a -> l -> b와 a -> b 중 어떤 것이 최단시간인지 비교하고 그 값을 graph[a][b]자리에 넣어준다.
# 이때 l은 거쳐가는 노드이므로 1에서 n까지 반복해준다.
# 플로이드 워셜 알고리즘, min을 이용한 점화식을 표현해야한다.
# 아래의 반복문이 완료되면 graph의 각 원소에는 a에서 b로 가는 최단 시간이 저장된다.
# graph의 원소가 INF 이상이면 경로가 존재하지 않음을 뜻한다.

for l in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][l] + graph[l][b])


# 최종 비용
total_cost = graph[1][k] + graph[k][x]

# 1 - k - x 경로가 존재하지 않는다는 것(-1 출력)은 graph[1][k]와 graph[k][x] 중 최소한 둘 중 하나는 INF 이상이라는 얘기이므로
# total_cost 는 그 경우 무조건 INF 이상의 값을 가진다.
if total_cost >= INF:
    print(-1)
else:
    print(total_cost)


# Input

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5


# 4 2
# 1 3
# 2 4
# 3 4








