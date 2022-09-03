# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    alpha = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    answer = ""
    for char in s:
        if not char.isalpha():
            answer += char
        else:
            idx = alpha.index(char.upper()) + n - 26 if alpha.index(char.upper()) + n > 26 else alpha.index(char.upper()) + n
            if char.isupper():
                answer += alpha[idx]
            else:
                answer += alpha[idx].lower()

    return answer