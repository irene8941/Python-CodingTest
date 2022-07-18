# https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=python3

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    cnt = {}                # report count
    check = {}              # personal report
    report = set(report)
    
    for row in report:
        key, value = row.split(' ')
        
        if value in cnt:
            cnt[value] += 1
        else:
            cnt[value] = 1
            
        if key not in check:
            check[key] = [value]
        else:
            check[key] += [value]
            
    for key, value in cnt.items():
        if value >= k:
            for fromId, toId in check.items():
                if key in toId:
                    answer[id_list.index(fromId)] += 1
            
    return answer