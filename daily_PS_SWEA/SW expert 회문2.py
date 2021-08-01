arr = [[0 for _ in range(100)] for _ in range(100)]
arr1 =[[0 for _ in range(100)] for _ in range(100)]
def same(x):
    L = len(x)
    for i in range(L // 2):
        if x[i] != x[L - i - 1]:
            return 0
    return 1

for i in range(10):
    TC = int(input())
    length = 100
    count = 0
    for j in range(100):
        arr[j] = list(input())
    for j in range(100):
        for k in range(100):
            arr1[j][k] = arr[k][j]
    for j in range(length, 0, -1):
        if count >= j:
            break
        for k in range(100):
            if count == j:
                break
            for x in range(101 - j):
                if same(arr[k][x:x+j]) or same(arr1[k][x:x+j]):
                    count = j
                    break

    print(("#%d %d" %(TC, count)))

