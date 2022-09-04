# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ""

    idx = 0
    for totIdx in range(len(s)):
        if not s[totIdx].isalpha():
            answer += s[totIdx]
            idx = 0
        else:
            answer += s[totIdx].upper() if idx % 2 == 0 else s[totIdx].lower()
            idx += 1

    return answer