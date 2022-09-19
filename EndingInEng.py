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
        person = n if (len(arr) + 1) % n == 0 else (len(arr) + 1) % n
        turn = (len(arr) + 1) // n if (len(arr) + 1) % n == 0 else (len(arr) + 1) // n + 1
        return [person, turn]