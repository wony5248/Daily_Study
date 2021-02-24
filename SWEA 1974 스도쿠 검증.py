T = int(input())
for i in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    serosudoku = [[0 for _ in range(9)] for _ in range(9)]
    isgaro = 1
    issero = 1
    issquare = 1
    result = 0
    for garo in range(9):
        lst = list(set(sudoku[garo]))
        if len(lst) != 9:
            isgaro = 0
    for j in range(9):
        for k in range(9):
            serosudoku[j][k] = sudoku[k][j]
    for sero in range(9):
        serolst = list(set(serosudoku[sero]))
        if len(serolst) != 9:
            issero = 0
    for j in range(0, 7, 3):
        for k in range(0, 7, 3):
            sumV = 0
            for l in range(j, j+3):
                for m in range(k, k+3):
                    sumV += sudoku[l][m]
            if sumV != 45:
                issquare = 0
    if isgaro == 1 and issero ==1 and issquare ==1:
        result =1
    # print(isgaro)
    # print(issero)
    # print(issquare)
    print("#%d %d" %(i+1, result))