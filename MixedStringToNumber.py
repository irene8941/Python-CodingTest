# https://school.programmers.co.kr/learn/courses/30/lessons/81301#

def solution(s):
    answer = ""
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    a = 0
    while a < len(s):
        # 이미 숫자인 경우
        if s[a].isdigit():
            answer += str(s[a])
            a += 1
        # 영어인 경우
        else:
            word = s[a]
            for b in range(a + 1, len(s)):
                if s[b].isdigit():
                    answer += str(words.index(word))
                    a = b + 1
                    break
                else:
                    word += s[b]
                    if word in words:
                        answer += str(words.index(word))
                        a = b + 1
                        break

    
    return int(answer)