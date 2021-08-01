def inorder(x):
    global result
    if x * 2 <= N:
        inorder(x * 2)

    result.append(data[x])

    if x * 2 + 1 <= N:
        inorder(x * 2 + 1)


for tc in range(1, 11):
    N = int(input())
    data = [[] for _ in range(N + 1)]
    for _ in range(N):
        a = list(input().split())
        data[int(a[0])] = a[1]
    result = []
    inorder(1)
    string = ""
    for i in result:
        string = string + i
    print("#%d %s" %(tc, string))