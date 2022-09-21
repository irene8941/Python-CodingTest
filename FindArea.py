# https://www.acmicpc.net/problem/2583

from collections import deque
def bfs(x, y):
    queue = deque([(x, y)])
    cnt = 1
    graph[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 0:
                cnt += 1
                graph[nx][ny] = 1
                queue.append((nx, ny))
    return cnt

# 가로길이 M, 세로길이 N, 직사각형 개수 K
m, n, k = map(int, input().split())

# 그래프
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(y1, y2):
        for y in range(x1, x2):
            graph[x][y] = 1

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))