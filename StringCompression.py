# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    # 문자 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        comp = ""       # 압축된 문자열 변수 초기화
        prev = s[:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1       # 압축 횟수 초기화
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 문자열과 동일하다면 압축 횟수(count) 증가
            if prev == s[j : j + step]:
                count += 1
            # 이전 문자열과 상이하다면(더 이상 압축하지 못하는 경우)
            else:
                comp += str(count) + prev if count >= 2 else prev   # 문자열 압축
                count = 1                                           # 압축 횟수 초기화                        
                prev = s[j : j + step]                              # 다음 문자열로 상태 초기화
        # 남아있는 문자열에 대하여 압축
        comp += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열 중 길이가 가장 짧은 문자열이 정답
        answer = min(answer, len(comp))
    return answer