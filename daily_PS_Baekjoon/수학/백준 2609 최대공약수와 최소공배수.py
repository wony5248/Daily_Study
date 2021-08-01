T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    lst = []
    bigv = max(x, y)
    smv = min(x, y)
    for i in range(1, bigv + 1):
        if x % i == 0 and y % i == 0:
            lst.append(i)
    lst.sort()
    maxv = max(lst)

    div = bigv / maxv
    minv = smv * div

    print("%d" % minv)