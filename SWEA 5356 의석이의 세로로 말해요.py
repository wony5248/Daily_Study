T = int(input())
for i in range(T):
    maxV = 0
    result = ""
    lst = [list(input()) for _ in range(5)]
    for j in range(5):
        if len(lst[j]) > maxV:
            maxV = len(lst[j])
    for j in range(5):
        while len(lst[j]) != maxV:
            lst[j].append("")
    for j in range(maxV):
        for k in range(5):
            result += lst[k][j]

    print("#%d %s" %(i+1, result))