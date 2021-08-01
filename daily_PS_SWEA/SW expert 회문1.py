arr = [[0 for _ in range(8)] for _ in range(8)]
arr1 =[[0 for _ in range(8)] for _ in range(8)]
def same(x):
    L = len(x)
    for i in range(L // 2):
        if x[i] != x[L - i - 1]:
            return 0
    return 1

for i in range(10):
    length = int(input())
    count = 0
    for j in range(8):
        arr[j] = list(input())
    for j in range(8):
        for k in range(8):
            arr1[j][k] = arr[k][j]
    for j in range(8):
        for k in range(9 - length):
            if same(arr[j][k:k + length]):
                count += 1
            if same(arr1[j][k:k + length]):
                count += 1

    print(("#%d %d" %(i+1, count)))
