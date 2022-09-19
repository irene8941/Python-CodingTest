def solution(n):
    cnt = bin(n)[2 : ].count('1')

    # 조건1
    for i in range(n + 1, 1000000):
        # 조건2
        if bin(i)[2 : ].count('1') == cnt:
            # 조건3
            return i