# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt0 = lottos.count(0)
    
    for w in win_nums:
        if w in lottos:
            answer += 1
    
    return [rank[answer + cnt0], rank[answer]]