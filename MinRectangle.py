# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    minList, maxList = [], []
    
    for w, h in sizes:
        minList.append(min(w, h))
        maxList.append(max(w, h))
    
    return max(minList) * max(maxList)