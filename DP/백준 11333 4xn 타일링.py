TC = int(input())

for i in range(TC):
    length = int(input())
    garo = [0 for _ in range(10001)]
    garo[0] = 1
    garo[3] = 3
    garo[6] = 13
    for j in range(9, length+1, 3):
        garo[j] = (5 * garo[j-3] - 3 * garo[j-6] + garo[j-9]) % 1000000007
    if length % 3 != 0:
        print(0)
    else:
        print(garo[length])
