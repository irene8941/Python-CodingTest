# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    result = []
    # LIFO 스택
    stack = list(s)
    while stack:
        # 괄호 하나 꺼내서
        a = stack.pop()
        # 비교 리스트에 비교할 괄호가 없으면
        if len(result) <= 0:
            result.append(a)    # 추가
            continue
        # 비교 리스트에서 비교할 괄호 (마지막 인덱스 괄호)
        b = result[len(result) - 1]
        # '()'을 만들 수 있으면
        if a + b == '()':
            result.pop()        # 비교 리스트에서 마지막 인덱스 괄호 제거
        else:
            result.append(a)    # 추가

    return False if len(result) > 0 else True