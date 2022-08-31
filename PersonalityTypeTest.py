def solution(survey, choices):
    scorArr = [0, 3, 2, 1, 0, 1, 2, 3]
    charArr = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    tbl =  {c: 0 for c in charArr}
    
    for s, c in zip(survey, choices):
        if c < 4:
            tbl[s[0]] += scorArr[c]
        else:
            tbl[s[1]] += scorArr[c]
    
    answer = ""
    for i in range(0, len(charArr), 2):
        left = charArr[i]
        right = charArr[i+1]
        
        if tbl[left] == tbl[right]:
            answer += min(left, right)
        else:
            answer += left if tbl[left] > tbl[right] else right

    return answer
            