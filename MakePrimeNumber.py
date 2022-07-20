# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations
import math

def solution(nums):
    sets = list(combinations(nums, 3))
    answer = len(sets)
    
    for s in sets:
        sumSet = sum(s)
        for i in range(2, int(math.sqrt(sumSet)) + 1):
            if sumSet % i == 0:
                answer -= 1
                break

    return answer