# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    arr = [words[0]]

    for idx in range(1, len(words)):
        pre = arr[len(arr) - 1][-1]
        now = words[idx]
        if len(now) > 1 and now not in arr and now[0] == pre:
            arr.append(now)
        else:
            break

    if len(arr) == len(words):
        return [0, 0]
    else:
        tmp = len(arr) + 1 # 탈락
        tmpTurn, tmpPer = divmod(tmp, n)
        turn = tmpTurn if tmpPer == 0 else tmpTurn + 1
        person = n if tmpPer == 0  else tmpPer
        return [person, turn]