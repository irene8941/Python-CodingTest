# https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    numSets = [ i for i in range(10)]
    return sum(list(set(numSets) - set(numbers)))