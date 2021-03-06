T = int(input())


def secure():
    global result
    for i in range(2, N+2):
        for j in range(N):
            for k in range(N):
                count = 0
                for x, y in home:
                    if abs(j - x) + abs(k - y) < i:
                        count += 1
                if count > result and count * M >= i ** 2 + (i-1) **2:
                    result = count



for tc in range(T):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    home = []
    for i in range(N):
        for j in range(N):
            if city[i][j]:
                home.append([i, j])
    result = 1
    secure()

    print("#%d %d" %(tc+1, result))