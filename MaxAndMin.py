# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    arr=list(map(int, s.split()))
    return str(min(arr)) + " " + str(max(arr))