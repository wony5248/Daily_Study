T = int(input())


for i in range(T):
    maxV = 0
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    for j in range(N-M+1):
        for k in range(N-M+1):
            result = 0
            for l in range(j, j+M):
                for m in range(k, k+M):
                    result += lst[l][m]
            if result > maxV:
                maxV = result

    print("#%d %d" %(i+1, maxV))