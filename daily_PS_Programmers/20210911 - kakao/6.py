def solution(board, skill):
    answer = 0
    for sk in skill:
        r1 = sk[1]
        c1 = sk[2]
        r2 = sk[3]
        c2 = sk[4]
        dmg = sk[5]
        if sk[0] == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] -= dmg
        elif sk[0] == 2:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] += dmg
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                answer += 1
    return answer