t = int(input())
result = ["" for i in range(t)]
home = [0 for i in range(2)]
k = 0
for i in range(t):
    n = int(input())
    lst = [[0 for i in range(2)] for j in range(n)]
    homex, homey = map(int, input().split())
    home = [homex,homey]
    for j in range(n):
        x, y = map(int, input().split())
        lst[j] = [x, y]
    destx, desty = map(int, input().split())
    dest = [destx, desty]


    visit = [0 for i in range(n)]
    result[i] ="sad"
    queue = list([home])
    while queue:
        me = queue.pop(0)
        homedest = abs(me[0] - destx) + abs(me[1] - desty)
        if homedest <= 1000:
            result[i] = "happy"
            break
        for k in range(n):
            distance = abs(me[0] - lst[k][0]) + abs(me[1] - lst[k][1])
            if visit[k] or distance > 1000:
                continue
            queue.append(lst[k])
            visit[k] = 1
for i in range(t):
    print(result[i])






