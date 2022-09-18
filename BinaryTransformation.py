# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    cnt0 = 0    # 제거한 0의 개수
    step = 0    # 이진 변환 횟수

    while s != "1":
        # x의 모든 0제거
        if s.count("0") > 0:
            cnt0 += s.count("0")
            s = s.replace("0", "")
        # 0 제거 후 길이
        s = len(s)
        # 이진 변환 결과
        temp = []
        step += 1
        while s > 1:
            if s % 2 == 0:
                temp.append("0")
            else:
                temp.append("1")
            s //= 2
        temp.append("1")
        temp.reverse()
        s = "".join(temp)

    return [step, cnt0]