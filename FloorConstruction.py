#  이것이코딩테스트다 p.223 바닥 공사

n = int(input())

# DP 테이블 초기화
d = [0] * 1001

# DP 구현
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])