# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    basket = [-1]
    
    for m in moves:
        for i in range(len(board)):
            item = board[i][m-1]
            if item != 0:
                if basket[-1] == item:
                    basket.pop(-1)
                    answer += 2
                else:
                    basket.append(item)
                board[i][m-1] = 0
                break

    return answer