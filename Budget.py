# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    cnt = [0] * (len(d) + 1)
    
    if d[0] <= budget:
        cnt[1] = 1
    
    for i in range(1, len(d)):
        if d[i - 1] + d[i] <= budget:
            d[i] += d[i - 1]
            cnt[i + 1] += cnt[i] + 1
    
    return max(cnt)