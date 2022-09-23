#  이것이코딩테스트다 p.220 개미 전사

# 식량창고의 개수
n = int(input())
# 각 식량창고에 저장된 식량의 개수
arr = list(map(int, input().split()))

# DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행(상향법)
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + arr[i])

# 계산된 결과 출력
print(d[n - 1])