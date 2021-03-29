n, m = map(int, input().split())
charater = list(map(int, input().split()))

maps = []
for i in range(n):
    a = list(map(int, input().split()))
    maps.append(a)

nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]


stack = []
cnt = 1
while True:
    if len(stack) == 4:
        l = stack.pop()
        x = charater[0]+nx[l-1] if l!=0 else charater[0]+nx[3]
        y = charater[1]+ny[l-1] if l!=0 else charater[1]+ny[3]

        if maps[x][y] == 0:
            maps[x][y] = 1
            charater = [x, y, loc]
            cnt += 1
            stack = []
        else:
            break


    x = charater[0]+nx[charater[2]]
    y = charater[1]+ny[charater[2]]
    loc = charater[2]-1 if charater[2]!=0 else 3
    if maps[x][y] == 0:
        maps[x][y] = 1
        charater = [x, y, loc]
        cnt += 1
        stack = []
    else:
        stack.append(charater[2])
        charater[2] = loc

print(cnt)