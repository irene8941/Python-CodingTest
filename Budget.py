# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    
    while sum(d) > budget:
        d.pop()
    
    return len(d)