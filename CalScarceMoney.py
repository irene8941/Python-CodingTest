# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = 0
    
    for i in range(1, count + 1):
        answer += price * i

    return -min(0, money - answer)