n = int(input())
k = int(input())

board = []
## board = [[0]*n]*n 이렇게 하니까 값 변경할 때 잘 안됨
board.append([1]*(n+2))
for i in range(n):
    li = []
    for j in range(n+2):
        if j == 0 or j == (n+1):li.append(1) # 외벽
        else: li.append(0)
    board.append(li)
board.append([1]*(n+2))

for i in range(k):
    x, y = map(int,input().split())
    board[x][y] = 2 # 사과 위치 표시


l = int(input())


print(board)
