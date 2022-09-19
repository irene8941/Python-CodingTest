# https://school.programmers.co.kr/learn/courses/30/lessons/12914#

def solution(n):
    d = [0] * (n + 1)
    try:
        d[1] = 1
        d[2] = 2
    except IndexError:
        return n

    for i in range(3, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 1234567

    return d[n]