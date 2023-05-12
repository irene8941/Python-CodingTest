# https://www.acmicpc.net/problem/1389

from collections import deque

def bfs(user):
    # 케빈 베이컨의 수이며, 방문처리 이력까지 포함
    # 방문하지 않은 유저: -1
    dist = [-1] * (N + 1)        
    dist[0] = dist[user] = 0

    q = deque([user])
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if dist[nx] == -1:  # 아직 방문하지 않은 유저를 방문
                dist[nx] = dist[x] + 1  # 연결
                q.append(nx)

    return sum(dist)

if __name__ == '__main__':
    # 유저의 수 N, 친구 관계의 수 M
    N, M = map(int, input().split())
    # 친구 관계
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)

    resultList = [0] * (N + 1) # 각 유저별 케빈 베이컨의 수
    for user in range(1, N + 1):
        resultList[user] = bfs(user)

    minUser = 1
    minAnswer = resultList[1]
    for i in range(2, N + 1):
        if resultList[i] < minAnswer:
            minUser = i
            minAnswer = resultList[i]
    print(minUser)