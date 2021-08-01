T = int(input())
for tc in range(T):
    n = int(input())
    result = []
    final = []
    nasa = list(map(int, input().split()))
    for i in range(0, n*2, 2):
        result.append([nasa[i], nasa[i+1]])
    final.append(result.pop(0))
    loc = 0
    while result:
        if result[loc][1] == final[0][0]:
            final.insert(0, result.pop(loc))
            loc = 0
        elif result[loc][0] == final[len(final) -1][1]:
            final.append(result.pop(loc))
            loc = 0
        else:
            loc += 1
    print("#%d" %(tc + 1), end=" ")
    for i in range(len(final)):
        print(final[i][0], end=" ")
        print(final[i][1], end=" ")
    print()
