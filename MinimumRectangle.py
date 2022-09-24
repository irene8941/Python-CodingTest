# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    xArr = []
    yArr = []

    for x, y in sizes:
        xArr.append(min(x, y))
        yArr.append(max(x, y))

    return max(xArr) * max(yArr)