from itertools import combinations
T = int(input())
for tc in range(T):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    lst = [[0] * (N - M + 1) for i in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            tmp = honey[i][j:j+M]
            result = 0
            for k in range(1, M + 1):
                for l in combinations(tmp, k):
                    if sum(l) <= C:
                        count = 0
                        for d in l:
                            count += d ** 2
                        if result < count:
                            result = count
            lst[i][j] = result


    final = 0
    for i in range(N):
        for j in range(N-M+1):
            lst2 = []
            lst2 += lst[i][j+M:N-M+1]
            for k in range(i+1, N):
                lst2 += lst[k]
            if lst2:
                result = lst[i][j] + max(lst2)
                if final < result:
                    final = result

    print("#%d %d" %(tc+1, final))