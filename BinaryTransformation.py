# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    cnt0 = 0    # 제거한 0의 개수
    step = 0    # 이진 변환 횟수

    while s != '1':
        step += 1
        cnt0 += s.count('0')    # 제거된 0의 개수
        cnt1 = s.count('1')     # 0제거 > 길이
        s = bin(cnt1)[2:]       # 2진법 변환

    return [step, cnt0]