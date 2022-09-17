# https://school.programmers.co.kr/learn/courses/30/lessons/12934

import math

def solution(n):
    temp = int(math.sqrt(n))
    return (temp + 1)**2 if temp**2 == n else -1