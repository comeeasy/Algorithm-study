from collections import deque

# 강의 개수
n = int(input())

# 각 강의가 갖는 선수과목의 개수
inegree = [0] * (n+1)

# 각 강의가 누구의 선수과목인지 제시
graph = [[]for i in range(n+1)]

# 각 강의의 개별 수강 시간
time = [0] * (n+1)

# 강의들의 관계에 관한 정보 입력
for i in range(1, n+1):
    l = list(map(int, input().split()))

#    for x in l[1:-1]:
#       for y in range(1, n+1):
#           if x == y:
#               graph[x].append(i)

#   if(l[1] != -1):
#       for x in l[1:-1]:
#           indegree[i] += 1

    for x in l[1:-1]:
        graph[x].append(i)
        indegree[i] += 1

    time[i] = l[0]

print(graph)
# [[], [2, 3, 4], [], [4, 5], [], []]
print(indegree)
# [0, 0, 1, 1, 2, 1]
print(time)
# [0, 10, 10, 4, 4, 3]

def topology_sort():
    q = deque()
    result = time
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)


    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                result[i] = result[now] + time[i]
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])

topology_sort()


