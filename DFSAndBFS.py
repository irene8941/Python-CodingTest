# https://www.acmicpc.net/problem/1260

from collections import deque
def dfs(v, graph, dfsVisited):
    stack = [v]
    while stack:
        node = stack.pop()
        if dfsVisited[node] != 0:
            continue
        dfsVisited[node] = 1
        print(node, end = ' ')
        for i in graph[node]:
            stack.append(i)

def bfs(v, graph, bfsVisited):
    q = deque([v])
    while q:
        node = q.popleft()
        if bfsVisited[node] != 0:
            continue
        bfsVisited[node] = 1
        print(node, end = ' ')
        for i in graph[node]:
            if bfsVisited[i] == 0:
                q.append(i)

# 정점 N, 간선 M, 시작점 V
n, m, v = map(int, input().split())

# 양방향 그래프
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
dfsVisited = [0] * (n + 1)
bfsVisited = [0] * (n + 1)

# 그래프 정렬
for i in range(n + 1):
    graph[i].sort(reverse = True)
dfs(v, graph, dfsVisited)
print()

# 그래프 정렬
for i in range(n + 1):
    graph[i].sort()
bfs(v, graph, bfsVisited)
