# https://school.programmers.co.kr/learn/courses/30/lessons/77884#

def solution(left, right):
    answer = 0
    
    for num in range(left, right + 1):
        cnt = 0
        for i in range(1, num + 1):
            if num % i == 0:
                cnt += 1
        answer += num if cnt % 2 == 0 else -num
    
    return answer