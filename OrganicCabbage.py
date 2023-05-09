import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 배추밭 범위를 벗어나는 경우
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        # 한 번도 방문하지 않은 배추인 경우
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx, ny)

# 테스트 케이스의 개수 t
t = int(input())
answer = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(t):
    # 배추밭의 가로길이 m, 세로길이 n, 배추가 심어져 있는 위치의 개수 k
    m, n, k = map(int, input().split())

    graph = [[0] * n for _ in range(m)] # 배추밭
    for _ in range(k):
        # 배추의 위치 (x, y)
        x, y = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                cnt += 1
                graph[i][j] = 0
                dfs(i, j)
    answer.append(cnt)

for i in answer: print(i)