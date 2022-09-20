from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0
    cnt = 0 # 단지 내 집의 수
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 지도의 범위를 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 방문하지 않은 아파트인 경우
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
    return cnt

# 지도의 크기
n = int(input())
# 지도
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
# 방향(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            arr.append(bfs(x, y))

print(len(arr))
arr.sort()
for a in arr:
    print(a)