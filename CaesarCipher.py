# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ""

    for char in s:
        if not char.isalpha():  # 공백
            answer += char
            continue
        if char.isupper():      # 대문자
            answer += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        else:                   # 소문자
            answer += chr((ord(char) - ord('a') + n) % 26 + ord('a'))

    return answer