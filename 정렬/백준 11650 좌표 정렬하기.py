N = int(input())
spot = [list(map(int, input().split())) for _ in range(N)]
spot.sort(key= lambda x : (x[0], x[1]))
for i in spot:
    print("%d %d" %(i[0], i[1]))