# DFS/BFS
## 꼭 필요한 자료구조 기초
**탐색(Search)** : 많은 양의 데이터 중 원하는 데이터를 찾는 과정
**자료구조(Data Structure)** : 데이터를 표현하고 관리하고 처리하기 위한 구조
- 삽입(Push) : 데이터를 삽입한다
  - overflow : 특정 자료구조(스택, 큐 ...)가 사용할 수 있는 데이터 크기를 이미 가득 찬 상태에서 삽입연산 수행
- 삭제(Pop) : 데이터를 삭제한다
  - underflow : 특정 자료구조에 데이터 들어있지 않은 상태에서 삭제 연산 수행


### 스택(Stack)
**선입후출(First In Last Out, FILO) 혹은 후입선출(Last In First Out, LIFO)**
- 파이썬에서는 리스트로 구현.
```python
stack = [] # 스택 생성

stack.append(5) # push
stack.pop() # pop
```
### 큐(Queue)
**선입선출(First In First Out, FIFO)**
- 파이썬에서는 `deque`로 구현.
```python
from collection import deque

queue = deque() # 큐 생성

#push
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)


#pop
queue.popleft()
queue.popleft()
```
### 재귀함수(Recursive Function)
자기 자신을 다시 호출하는 함수.
```python
def recursive_function():
    print("재귀함수 호출")
    recursive_fucntion()

recurcive_function()
```
- 재귀함수로 문제를풀 때는 재귀함수가 언제 끝날지 **종료조건** 꼭 명시해야 함.

## 탐색 알고리즘 DFS/BFS
### DFS(Depth-First Search, 깊이 우선 탐색)
그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
#### 그래프(Graph)
- 노드(node)와 간선(edge)으로 표현되며, 노드를 정점(vertex)이라고도 함.
- 인접행렬(Adjacency Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
  - 메모리 측면 : 메모리가 불필요하게 낭비
- 인접리스트(Adjacency List) : 리스트로 그래프의 연결 관계 표현하는 방식
  - 메모리 측면 : 메모리 효율적으로 사용
  - 두 노드 연결되어있는지 정보 얻는 속도 느림

#### DFS는?
스택 자료구조를 사용
1. 탐색 시작 노드를 스택에 삽입하고 방문처리.
2. 스택 최상단 노드에 방문하지 않은 인접노드 있으면 그 인접노드 스택에 넣고 방문처리. 방문하지 않은 인접노드 없어지면 스택에서 최상단 노드 꺼냄
3. 2번 과정을 더이상 수행할 수 없을 때까지 반복.

```python
def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    prnt(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드 연결된 정보 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드 방문된 정보 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

### BFS(Breadth Frist Search, 너비 우선 탐색)
가까운 노드부터 탐색하는 알고리즘
1. 탐색 시작 노드를 큐에 삽입하고 방문처리
2. 큐에서 노드를 꺼내 해당 노드 인접 노드 중 방문하지 않은 노드 모두 큐에 삽입하고 방문처리
3. 2번 과정 더이상 수행할 수 없을 때까지 반복

```python
from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문처리
    visited[start] = True
    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드 연결된 정보 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드 방문된 정보 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```

#### DFS vs BFS
||DFS|BFS|
|--|----|----|
|동작 원리|스택|큐|
|구현 방법|재귀 함수 사용|큐 자료구조 이용|