# https://www.acmicpc.net/problem/2178

from collections import deque

# 동서남북 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로의 범위를 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 미로에서 이동할 수 있는 칸이고
            if graph[nx][ny] == 1:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True          # 방문처리
                    dist[nx][ny] = dist[x][y] + 1   # 최소의 칸 수 저장
                    queue.append((nx, ny))

# N x M
N, M = map(int, input().split())
# 미로
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
# 해당 칸을 이동할 때 지나가는 최소 칸의 수 배열
dist = [[0] * M for _ in range(N)]
# 방문처리 배열
visited = [[False] * M for _ in range(N)]

dist[0][0] = 1
visited[0][0] = True

bfs(0, 0)
print(dist[N - 1][M - 1])