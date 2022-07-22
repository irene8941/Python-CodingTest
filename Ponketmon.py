# https://school.programmers.co.kr/learn/courses/30/lessons/1845

from itertools import combinations

def solution(nums):
    return min(len(nums) // 2, len(set(nums)))