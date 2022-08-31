# https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3

def solution(survey, choices):
    scores = [0, 3, 2, 1, 0, 1, 2, 3]
    charr = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    labes =  {c: 0 for c in charr}
    
    for s, c in zip(survey, choices):
        if c == 4:
            continue
        elif c < 4:
            labes[s[0]] += scores[c]
        else:
            labes[s[1]] += scores[c]
    
    answer = ""
    for i in range(0, len(charr), 2):
        now = charr[i:i+2]
        if labes[now[0]] == labes[now[-1]]:
            answer += sorted(now)[0]
        elif labes[now[0]] > labes[now[-1]]:
            answer += charr[i]
        else:
            answer += charr[i+1]

    return answer
            