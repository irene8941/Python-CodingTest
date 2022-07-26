# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    return max(min(s) for s in sizes) * max(max(s) for s in sizes)