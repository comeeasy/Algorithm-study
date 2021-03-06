# BFS는 답이 되는 경로가 여러개여도 최단경로를 보장

# queue 사용
from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 상하좌우
dirN = [-1, 1, 0, 0]
dirM = [0, 0, -1, 1]


def bfs(n, m):
    queue = deque()
    queue.append((n, m))
    count = 0
    # 큐가 빌때까지 반복
    while queue:
        # 방문
        n, m = queue.popleft()

        # 방향별로 확인
        for k in range(4):
            new_n = n + dirN[k]
            new_m = m + dirM[k]

            # 다음 방향이 범위 밖의 위치이면
            if new_n <= 0 or new_n >= N or new_m <= 0 or new_m >= M:
            # 다른 방향 모색
                continue

            # 다음 방향에 0이거나 2가 있으면
            if graph[new_n][new_m] == 0 or graph[new_n][new_m] == 2:
            # 다른 방향 모색
                continue

            # 다음 방향에 1이 있으면
            if graph[new_n][new_m] == 1:
                graph[new_n][new_m] += 1
                queue.append((new_n, new_m))

    for p in range(N):
        for q in range(M):
            if graph[p][q] == 2:
                count += 1

    return count + 1


print(bfs(0, 0))
