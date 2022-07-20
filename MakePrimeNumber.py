# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations
import math

def solution(nums):
    sets = list(combinations(nums, 3))
    answer = 0
    
    for s in sets:
        sumSet = sum(s)
        for i in range(2, int(math.sqrt(sumSet)) + 1):
            if sumSet % i == 0:
                break
        else: 
            answer += 1

    return answer