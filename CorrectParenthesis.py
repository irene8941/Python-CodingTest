# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = []

    for p in s:
        if p == '(':
            answer.append(p)
        else:
            try:
                answer.pop()
            except IndexError:
                return False

    return len(answer) == 0