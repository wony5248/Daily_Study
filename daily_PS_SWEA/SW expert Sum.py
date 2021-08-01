for _ in range(10):
    Tnum = int(input())
    xsum = [0 for _ in range(100)]
    ysum = [0 for _ in range(100)]
    lzsum = 0
    rzsum = 0
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))
        xsum[i] = sum(arr[i])
    for j in range(100):
        lzsum += arr[j][j]
        rzsum += arr[j][99 - j]
        for k in range(100):
            ysum[j] += arr[k][j]

    all = list()
    xmax = max(xsum)
    all.append(xmax)
    ymax = max(ysum)
    all.append(ymax)
    all.append(lzsum)
    all.append(rzsum)
    print("#%d" %(Tnum), end=" ")
    print(max(all))
