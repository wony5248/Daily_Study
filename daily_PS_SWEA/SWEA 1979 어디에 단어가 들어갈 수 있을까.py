T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    trans = [[0 for _ in range(N)] for _ in range(N)]

    result = 0
    for j in range(N):
        for l in range(N):
            trans[j][l] = puzzle[l][j]

    for j in range(N):
        for k in range(N - K + 1):
            x = k
            while x < N and puzzle[j][x] == 1:
                puzzle[j][x] = 0
                x += 1

            if x - k == K:
                result += 1

    for j in range(N):
        for k in range(N - K + 1):
            x = k
            while x < N and trans[j][x] == 1:
                trans[j][x] = 0
                x += 1

            if x - k == K:
                result += 1

    print("#%d %d" % (i+1, result))
