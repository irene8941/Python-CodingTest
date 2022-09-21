# https://www.acmicpc.net/problem/2178

from collections import deque

# NXM 미로
n, m = map(int, input().split())
# 미로
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 미로의 범위를 벗어난 경우
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

print(graph[n - 1][m - 1])