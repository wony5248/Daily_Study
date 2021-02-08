TC = int(input())
for i in range(TC):
    length = int(input())
    garo = [0 for _ in range(length+1)]
    garo[3] = 3
    for j in range(6, length+1):
        garo[j] = 3 * garo[j-3]
    print(garo[length] % 1000000007)