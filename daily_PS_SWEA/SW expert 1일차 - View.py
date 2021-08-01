for i in range(10):
    count = 0
    T = int(input())
    lst = list()
    building = list(map(int, input().split()))
    for k in range(2, T-2):
        if building[k] > building[k-1] and building[k] > building[k-2] and building[k] > building[k+1] and building[k] > building[k+2]:
            tmin = min(building[k] - building[k-1], building[k] - building[k-2], building[k] - building[k+1],building[k] - building[k+2])
            lst.append(tmin)
    for l in range(len(lst)):
        count += lst[l]
    print("#%d %d" %(i+1, count))