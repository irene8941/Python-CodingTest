# 이것이 코딩테스트다 p.217 1로 만들기

x = int(input())

d = [0] * (x + 1)

for i in range(2, x + 1):
    # d. x에서 1을 뺀다
    d[i] = d[i - 1] + 1
    # a. x가 5로 나누어떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    # b. x가 3으로 나누어떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # b. x가 2으로 나누어떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[x])