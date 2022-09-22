# https://www.acmicpc.net/problem/1012

from collections import deque

def bfs(x, y, graph, m, n):
    queue = deque([(x, y)])
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

# 테스트 케이스의 개수 T
t = int(input())
# 테스트 케이스 별 배추희지렁이 마리 수
answer = []

for _ in range(t):
    # 배추밭의 가로길이 M, 세로길이 N, 배추가 심어져 있는 위치의 개수 K
    m, n, k = map(int, input().split())
    # 그래프
    graph = [[0] * n for _ in range(m)]
    # 배추의 위치
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    # 방문방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = 0
    for x in range(m):
        for y in range(n):
            if graph[x][y] == 1:
                cnt += 1
                bfs(x, y, graph, m, n)
    answer.append(cnt)

for i in answer: print(i)