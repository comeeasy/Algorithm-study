from collections import deque

n, l, r = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]  # 행
dy = [0, 0, 1, -1]  # 열


def bfs(x, y):
    q = deque()
    q.append((x, y))

    # 연합의 총 인구수, 나라
    yeonhap_total = 0
    count = 0

    visited[x][y] = 1
    yeonhap = []

    while q:
        X, Y = q.popleft()

        # 연합에 속해 있는 국가의 수 count
        count += 1

        # 연합에 현재 위치 추가
        yeonhap.append((X, Y))

        # 연합의 총 인구수
        yeonhap_total += A[X][Y]

        for i in range(4):
            nx = X + dx[i]
            ny = Y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(A[X][Y] - A[nx][ny]) <= r:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    for x, y in yeonhap:
        A[x][y] = yeonhap_total // count

    if count == 1:
        return 0
    return 1

res = 0


# while문을 돌린 만큼 인구이동이 일어남
while True:
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                cnt += bfs(i, j)
                print(visited)

    for i in range(n):
        print(A[i])

    if cnt == 0:
        break
    res += 1

print(res)










