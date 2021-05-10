import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 10억

# 노드 개수, 간선 개수 입력받음
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 방문한 적 있는지 체크하는 목적의 리스트 만들기
visited = [False]* (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)