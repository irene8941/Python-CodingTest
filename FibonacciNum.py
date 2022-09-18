# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    d = [0] * (n + 1)
    d[0] = 0
    d[1] = 1

    for i in range(2, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 1234567

    return d[n]