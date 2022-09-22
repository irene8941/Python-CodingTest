# https://www.acmicpc.net/problem/2606

from collections import deque

# BFS 구현
def bfs(start):
    queue = deque([start])
    visited[start] = 1
    cnt = 0
    while queue:
        node = queue.popleft()
        if len(net[node]) > 0:
            for next_node in net[node]:
                if visited[next_node] == 0:
                    queue.append(next_node)
                    visited[next_node] = 1
                    cnt += 1
    return cnt


# 컴퓨터 수 : comp
comp = int(input())
# 연결 쌍 수 : pair
pair = int(input())
# 네트워크 초기화
net = [[] for _ in range(comp + 1)]
# 연결 컴퓨터 쌍 번호
for _ in range(pair):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)    # 양방향 간선임을 명심!
# 방문처리(0: 방문X, 1:방문O)
visited = [0 for _ in range(comp + 1)]

print(bfs(1))