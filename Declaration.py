# https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=python3

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    reports = {x : 0 for x in id_list}
    
    for r in report:
        reports[r.split()[1]] += 1
    
    for r in report:
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
        
    return answer