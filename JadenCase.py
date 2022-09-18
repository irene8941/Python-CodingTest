# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = s[0].upper()
    for idx in range(1, len(s)):
        if s[idx] == " ":
            answer += " "
        else:
            answer += s[idx].upper() if answer[idx - 1] == " " else s[idx].lower()

    return answer