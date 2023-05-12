# https://www.acmicpc.net/problem/1697

from collections import deque

def bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()
        # 수빈이가 동생에게 도달한 경우
        if x == K:
            return
        for nx in (x - 1, x + 1, 2 * x):
            # 그래프를 벗어나는 경우
            if nx < 0 or nx > maxNum:
                continue
            # 한번도 방문하지 않은 경우
            if dist[nx] == 0:
                dist[nx] = dist[x] + 1
                q.append(nx)

# 수빈위치 N, 동생위치 K
N, K = map(int, input().split())
maxNum = 100000
dist = [0] * (maxNum + 1)

bfs()
print(dist[K])