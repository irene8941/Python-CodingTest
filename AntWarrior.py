#  이것이코딩테스트다 p.220 개미 전사

n = int(input())    # 식량창고의 개수
k = list(map(int, input().split()))   # 각 식량창고에 저장된 식량의 개수
d = [0] * n

for idx in range(n):
    if idx <= 1:
        d[idx] = k[idx]
    else:
        d[idx] = max(d[idx - 1], d[idx - 2] + k[idx])

print(max(d))