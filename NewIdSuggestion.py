# https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = ''
    # 1&2단계
    answer = re.sub('[^0-9a-z_.-]+', '', new_id.lower())
    # 3단계
    answer = re.sub('[..]+', '.', answer)
    # 4단계
    answer = answer.strip('.')
    # 5단계
    answer = "a" if answer == "" else answer
    # 6단계
    answer = answer[:15].rstrip('.')
    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer