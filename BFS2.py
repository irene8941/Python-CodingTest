# https://www.acmicpc.net/problem/24445

from collections import deque

# 정점(N), 간선(M), 시작 정점(R)
n, m, r = map(int, input().split())
# 양방향 간선 그래프
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (n + 1)
# 그래프 정렬
for i in range(n + 1):
    if len(graph[i]) > 0:
        graph[i].sort(reverse=True)
# BFS 구현
queue = deque([r])
cnt = 1
visited[r] = cnt
while queue:
    nn = queue.popleft()
    for nx in graph[nn]:
        if visited[nx] == 0:
            cnt += 1
            queue.append(nx)
            visited[nx] = cnt
# 답
for i in visited[1:]:
    print(i)