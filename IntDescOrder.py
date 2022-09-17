# https://school.programmers.co.kr/learn/courses/30/lessons/12933?language=python3

def solution(n):
    arr = [i for i in str(n)]
    arr.sort(reverse=True)
    return int("".join(arr))