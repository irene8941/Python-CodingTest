# https://school.programmers.co.kr/learn/courses/30/lessons/43163

def diff(now, new):
    count = 0
    for i, j in zip(now, new):
        if i != j:
            count += 1
    return True if count == 1 else False

def func(begin, target, words, visited):
    stack = [begin]
    count = -1
    while stack:
        now = stack.pop()
        count += 1
        if now == target:
            return count
        for idx in range(len(words)):
            if not visited[idx] and diff(now, words[idx]):
                visited[idx] = True
                stack.append(words[idx])

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False for _ in range(len(words))]

    return func(begin, target, words, visited)