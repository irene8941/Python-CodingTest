# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))