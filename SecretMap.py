# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        a = bin(a1 | a2)[2:]
        a = a.zfill(n)
        a = a.replace('1', '#').replace('0', ' ')
        answer.append(a)
        
    return answer