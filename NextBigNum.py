# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    # 조건1
    for i in range(n+ 1, 1000000):
        # 조건2
        if bin(i)[2:].count('1') == bin(n)[2:].count('1'):
            return i