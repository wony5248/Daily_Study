def cal(start):
    for i in range(start, 0, -1):
        if not data[i][0].isdecimal():
            x = int(data[int(data[i][1])][0])
            y = int(data[int(data[i][2])][0])
            if data[i][0] == "*":
                data[i][0] = x * y
            if data[i][0] == "/":
                data[i][0] = x / y
            if data[i][0] == "+":
                data[i][0] = x + y
            if data[i][0] == "-":
                data[i][0] = x - y




for tc in range(1, 11):
    N = int(input())
    data = [[] for _ in range(N + 1)]
    count = []
    for _ in range(N):
        a = list(input().split())
        data[int(a[0])] = a[1:]
        count.append(int(a[0]))
    maxnum = max(count)
    cal(maxnum)


    print("#%d %d" %(tc, data[1][0]))

