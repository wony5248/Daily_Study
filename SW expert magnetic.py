for l in range(10):
    count = [0 for _ in range(10)]
    N = int(input())
    magnetic = [[0 for _ in range(N)] for _ in range(N)]
    for k in range(N):
        magnetic[k] = list(map(int, input().split()))
    count[l] = 0
    for i in range(N):
        for j in range(N-1):
            if magnetic[j][i] == 1 and magnetic[j+1][i] == 0:
                magnetic[j][i] = 0
                magnetic[j+1][i] = 1
            elif magnetic[j][i] == 1 and magnetic[j+1][i] == 2:
                count[l] += 1
    print("#%d %d"%(l+1,count[l]))








