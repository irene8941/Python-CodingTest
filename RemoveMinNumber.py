# https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    minNum = min(arr)
    answer = []
    for a in arr:
        if minNum != a:
            answer.append(a)
    return answer if len(answer) else [-1]