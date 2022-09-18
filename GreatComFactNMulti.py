# https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    maxNum = max(n, m)

    ans1 = 1
    for i in range(1, maxNum // 2 + 1):
        if n % i == 0 and m % i == 0:
            ans1 = i if ans1 < i else ans1

    ans2 = (n // ans1) * (m // ans1) * ans1

    return [ans1, ans2]