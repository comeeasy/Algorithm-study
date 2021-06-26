
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, k, l):
    k = find_parent(parent, k)
    l = find_parent(parent, l)
    if k < l:
        parent[l] = k
    else:
        parent[k] = l


n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

edges = []
result = 0

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# c로 edges sorting 하기
edges.sort(key=lambda t: t[2])


for edge in edges:
    # edge 정보에 들어 있는 v1 v2는 둘 사이에 길이 있는 관계
    v1, v2, cost = edge
    # 사이클이 아니면
    if find_parent(parent, v1) != find_parent(parent, v2):
        union_parent(parent, v1, v2)
        result += cost
        max_cost = cost


print(result-max_cost)




