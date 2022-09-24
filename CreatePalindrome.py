# https://www.acmicpc.net/problem/1213

str = [i for i in input()]
str.sort()  # 사전 순 출력 대비

d = dict()
for s in str:
    d[s] = str.count(s)

center = ''
for s, i in d.items():
    if i % 2 != 0:
        if center == '':
            center = s
        else:
            print("I'm Sorry Hansoo")
            break
else:
    answer = ''
    for s, v in d.items():
        answer += s * (v // 2)
    answer += center + answer[::-1]
    print(answer)