# https://school.programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    arr.sort(reverse = True)
    answer = arr.pop()
    while arr:
        num = arr.pop()
        for i in range(min(answer, num), 0, -1):
            if answer % i == 0 and num % i == 0:
                answer = i * (answer // i) * (num // i)
                break
    return answer