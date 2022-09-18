# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        tot = i
        nxt = i
        while tot < n:
            nxt += 1
            tot += nxt
        if tot == n:
            answer += 1

    return answer