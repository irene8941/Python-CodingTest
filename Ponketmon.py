# https://school.programmers.co.kr/learn/courses/30/lessons/1845

from itertools import combinations

def solution(nums):
    numsSetLen = len(set(nums))
    numsLenHalf = len(nums) // 2
    return numsSetLen if numsLenHalf > numsSetLen else numsLenHalf