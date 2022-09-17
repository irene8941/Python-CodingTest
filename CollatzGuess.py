# https://school.programmers.co.kr/learn/courses/30/lessons/12943#

def solution(num):
    cnt = 0

    while num > 1:
        cnt += 1
        # 1-1
        if num % 2 == 0:
            num //= 2
        # 1-2
        else:
            num = num * 3 + 1
        if cnt == 500:
            return -1

    return cnt