# https://school.programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict

def solution(tickets):
    # 경로 정리
    tickets.sort(reverse=True)
    tick = defaultdict(list)
    for a, b in tickets:
        tick[a].append(b)

    stack = ['ICN']
    answer = []
    while stack:
        nxt = stack[-1]
        if tick[nxt] != []:
            stack.append(tick[nxt].pop())
        else:
            answer.append(stack.pop())

    return answer[::-1]
