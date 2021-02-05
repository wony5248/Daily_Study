

def preorder(x):
    global com
    com.append(data[x])
    if x + 1 <= N:
        preorder(x+1)



for tc in range(1, 11):
    N = int(input())
    data = [[] for _ in range(N + 1)]
    for _ in range(N):
        a = list(input().split())
        data[int(a[0])] = a[1]
    result = []
    com = []

    preorder(1)

    string1 = ""

    for j in com:
        string1 = string1 + " " + j
    print("#pre %d %s" % (tc, string1))