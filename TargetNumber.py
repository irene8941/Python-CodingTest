# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    result = [0]

    for n in numbers:
        temp = []
        for r in result:
            temp.append(r - n)
            temp.append(r + n)
        result = temp

    return result.count(target)