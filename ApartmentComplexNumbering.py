# https://www.acmicpc.net/problem/2667

def bfs(x, y):
    cnt = 0
    queue = [(x, y)]
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 지도를 벗어난 경우
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = 1
    return cnt

# 지도의 크기
N = int(input())
# 지도
# 1: 집이 있는 곳
# 0: 집이 없는 곳 또는 이미 방문한 집
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
# 방문처리
visited = [[0] * N for _ in range(N)]
# 방문방향(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

totCnt = 0
cntArr = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            totCnt += 1
            cntArr.append(bfs(i, j))
cntArr.sort()

print(len(cntArr))
for a in cntArr:
    print(a)