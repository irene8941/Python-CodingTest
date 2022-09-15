# https://www.acmicpc.net/problem/24444

from collections import deque

# 정점(N), 간선(M), 시작정점(R)
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(n + 1):
    if len(graph[i]) > 0:
        graph[i].sort()

queue = deque([r])
cnt = 1
visited[r] = cnt
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            visited[i] = cnt
            queue.append(i)

for i in visited[1:]:
    print(i)