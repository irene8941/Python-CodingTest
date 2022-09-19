# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []

    for word in s:
        if len(stack) == 0:
            stack.append(word)
        elif stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)

    return 1 if len(stack) == 0 else 0