# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    visited = [False] * n
    answer = 0

    def dfs(start):
        stack = [start]
        while stack:
            node = stack.pop()
            visited[node] = True
            for j in range(n):
                if computers[node][j] == 1 and not visited[j]:
                    stack.append(j)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer