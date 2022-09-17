# https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    arr = [int(i) for i in str(x)]
    total = sum(arr)
    return x % total == 0