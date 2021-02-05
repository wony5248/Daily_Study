def inorder(x):
    global result
    if x * 2 <= N:
        inorder(x * 2)

    result.append(data[x])

    if x * 2 + 1 <= N:
        inorder(x * 2 + 1)

final = [0, ]
for tc in range(1, 11):
    N = int(input())
    data = [[] for _ in range(N + 1)]
    for _ in range(N):
        a = list(input().split())
        data[int(a[0])] = a[1]
    result = []
    inorder(1)

    for j in range(1, len(result)-1):
        if result[j] == "+":
            if not result[j-1].isdecimal() or not result[j+1].isdecimal():
                final.append(0)
                break
        if result[j] == "*":
            if not result[j-1].isdecimal() or not result[j+1].isdecimal():
                final.append(0)
                break
        if result[j] == "/":
            if not result[j-1].isdecimal() or not result[j+1].isdecimal():
                final.append(0)
                break
        if result[j] == "-":
            if not result[j-1].isdecimal() or not result[j+1].isdecimal():
                final.append(0)
                break
        if result[j].isdecimal():
            if result[j-1].isdecimal() or result[j+1].isdecimal():
                final.append(0)
                break
        if j == len(result)-2:
            if result[j].isdecimal():
                if result[j - 1].isdecimal() or result[j + 1].isdecimal():
                    final.append(0)
                else:
                    final.append(1)
            else:
                if result[j - 1].isdecimal() or result[j + 1].isdecimal():
                    final.append(1)
                else:
                    final.append(0)
    print("#%d %d" %(tc, final[tc]))