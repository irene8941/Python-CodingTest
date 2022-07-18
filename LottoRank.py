# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    todo = list(set(win_nums) - set(lottos))
    todoLen = len(todo)
    zeroCnt = lottos.count(0)
    
    if todoLen == 0:
        answer = [1, 1]
    elif zeroCnt == 6:
        answer = [1, 6]
    elif todoLen == 6 and zeroCnt == 0:
        answer = [6, 6]
    else:
        answer = [1+(todoLen-zeroCnt), todoLen + 1]
    return answer