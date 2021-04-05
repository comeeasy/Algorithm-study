
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque() # 큐 생성
    queue.append((x, y))

    while queue: # 큐가 빌 때 까지
        x, y = queue.popleft()

        # 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위넘으면
                continue
            if graph[nx][ny] == 0: # 괴물 있으면
                continue
            if graph[nx][ny] == 1: # 괴물 없고 처음 방문하면
                graph[nx][ny] = graph[x][y] + 1 # 최단거리 기록
                queue.append((nx, ny))
    
    return graph[n-1][m-1] #(n,m) 최단거리 반환

print(bfs(0,0))
