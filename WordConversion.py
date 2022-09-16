# https://school.programmers.co.kr/learn/courses/30/lessons/43163

def diff(now, nxt):
    count = 0
    for w, t in zip(now, nxt):
        if w == t:
            continue
        count += 1
    return count

def solution(begin, target, words):
    visited = [False for _ in range(len(words))]
    count = -1

    if target not in words:
        return 0

    stack = [begin]
    while stack:
        now = stack.pop()
        count += 1
        if target == now:
            return count
        for idx in range(len(words)):
            if visited[idx]:
                continue
            if diff(now, words[idx]) == 1:
                   visited[idx] = True
                   stack.append(words[idx])

    return count