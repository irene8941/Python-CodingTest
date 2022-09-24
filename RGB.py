# https://www.acmicpc.net/problem/1149

n = int(input())    # 집의 수
graph = []
for _ in range(n):
    # 빨강, 초록, 파랑 비용
    graph.append(list(map(int, input().split())))
for i in range(1, n):
    graph[i][0] += min(graph[i - 1][1], graph[i - 1][2])
    graph[i][1] += min(graph[i - 1][0], graph[i - 1][2])
    graph[i][2] += min(graph[i - 1][0], graph[i - 1][1])

print(min(graph[n - 1]))