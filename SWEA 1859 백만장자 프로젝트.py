T = int(input())
for i in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    result = 0
    end= lst[-1]
    for j in range(len(lst)-1, -1, -1):
        if end > lst[j]:
            result += end - lst[j]
        else:
            end = lst[j]

    print("#%d %d" %(i+1, result))

