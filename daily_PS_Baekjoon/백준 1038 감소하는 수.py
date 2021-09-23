N = int(input())
cnt = 1
result = 0
if N >= 1023:
    print(-1)
elif N == 0:
    print(0)

else:
    while True:
        strcnt = str(cnt)
        isfalse = 0
        for i in range(len(strcnt) - 1):
            if int(strcnt[i]) > int(strcnt[i + 1]):
                continue
            else:
                cnt = int(strcnt[:i] + str(int(strcnt[i]) + 1) + "0" + strcnt[i + 2:])
                isfalse = 1
                break
        if isfalse == 0:
            result += 1
            if result == N:
                break
            cnt += 1

    print(cnt)