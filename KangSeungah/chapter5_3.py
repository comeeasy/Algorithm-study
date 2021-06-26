# 전체 크기 행과 열 입력받기
N, M = map(int, input().split())

# 0, 1 입력받기
graph = []
for i in range(N):  # graph 리스트에 N(행의 수)만큼 반복해서 각 행마다 원소 입력받기
    graph.append(list(map(int, input())))

# 0끼리 상하좌우로 연결되어있는 덩어리의 갯수가 알고싶은 것
# 인접한 0의 좌표를 모두 알고 싶은 것이므로 (상,하,좌,우에 대한 좌표의 값을 모두 알고 싶은 것) 재귀적으로 함수를 짜야함
# 하나의 덩어리에서(아이스크림이 만들어질 수 있는 칸) 인접한 0들이 모두 체크가 될때까지 함수를 호출
# 0이 확인 된 좌표는 1로 바꾸어줌(방문 처리)
# 0인지 아닌지 확인 후 0 이면 True 아니면 False를 반환
# DFS 실행

def dfs(n, m):
    # 0이 확인 된 좌표는 1로 바꾸어줌(방문 처리)
    if graph[n][m] == 0:
        graph[n][m] = 1  # 방문처리

        # 0인 노드에 대해 각각 재귀적으로 진행
        dfs(n+1, m)  # 상
        dfs(n-1, m)  # 하
        dfs(n, m-1)  # 좌
        dfs(n, m+1)  # 우
        return True
    return False  # 0이 아니면

    # 얼음 틀 밖의 수에 접근
    if n <= -1 or n >= N or m <= -1 or m >= M:
        return False


count = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)

