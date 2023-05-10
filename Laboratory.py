# https://www.acmicpc.net/problem/14502

from collections import deque
import copy

def bfs():
    queue = deque()
    this_map = copy.deepcopy(graph)
    
    for i in range(n):
        for j in range(m):
            if this_map[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if this_map[nx][ny] == 0:
                this_map[nx][ny] = 2
                queue.append((nx, ny))
    
    global answer
    cnt = 0
    for i in range(n):
        for j in range(m):
            if this_map[i][j] == 0: # 안전 영역 카운트
                cnt += 1
    
    answer = max(answer, cnt)

def make_wall(cnt):
    # 벽을 모두 세운 경우
    if cnt == 3:
        bfs()   # bfs 시작
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0 # 지도 복구



# 세로N, 가로M
n, m = map(int, input().split())
# 초기 지도
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 안전 영역의 최대 크기
answer = 0
make_wall(0)

print(answer)