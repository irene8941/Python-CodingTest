from collections import deque

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

def bfs():
    while q:
        x, y = q.popleft()
        z = C - x - y

        if x == 0:
            answer.append(z)
        # x -> y
        water = min(x, B - y)
        pour(x - water, y + water)
        # x -> z
        water = min(x, C - z)
        pour(x - water, y)
        # y -> x
        water = min(y, A - x)
        pour(x + water, y - water)
        # y -> z
        water = min(y, C - z)
        pour(x, y - water)
        # z -> x
        water = min(z, A - x)
        pour(x + water, y)
        # z -> y
        water = min(z, B - y)
        pour(x, y + water)

# 부피
A, B, C = map(int, input().split())

# 큐
q = deque()
q.append((0, 0))

# 방문여부
visited = [[False] * (B + 1) for _ in range(A + 1)]
visited[0][0] = True

# 답
answer = []

bfs()

answer.sort()
for a in answer: print(a, end = ' ')