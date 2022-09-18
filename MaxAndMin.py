# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    arr=list(map(int, s.split()))
    arr.sort()

    return str(arr[0]) + " " + str(arr[len(arr) - 1])