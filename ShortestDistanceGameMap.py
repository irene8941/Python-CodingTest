# https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3

from collections import deque

def solution(maps):
    # 동서남북
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    n = len(maps)
    m = len(maps[0])

    queue = deque([(0,0)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵에서 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1