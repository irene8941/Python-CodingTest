# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    numArr = [1] + [2**i for i in range(1, n)] # 2진수 배열
    numArr.sort(reverse = True)

    map1 = []   # 지도1 복호화
    map2 = []   # 지도2 복호화
    
    for num in arr1:
        row1 = []
        for i in range(n):
            if num >= numArr[i]:
                row1.append(1)
                num -= numArr[i]
            else:
                row1.append(0)
        map1.append(row1)

    for num in arr2:
        row2 = []
        for i in range(n):
            if num >= numArr[i]:
                row2.append(1)
                num -= numArr[i]
            else:
                row2.append(0)
        map2.append(row2)
        
    answer = []
    for i in range(n):
        answerRow = ""
        for j in range(n):
            if map1[i][j] == 1 or map2[i][j] == 1:
                answerRow += "#"
            else:
                answerRow += " "
        answer.append(answerRow)
        
    return answer