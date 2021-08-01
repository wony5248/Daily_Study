TC = int(input())
for i in range(TC):
    n = int(input())
    lst = [0 for k in range(11)]
    lst[1] = 1
    lst[2] = 2
    lst[3] = 4
    for j in range(4, n + 1):
        lst[j] = lst[j - 3] + lst[j - 2] + lst[j - 1]         # 마지막에 3 더해서 가능한 경우 2 더해서 가능한 경우 1더해서 가능한 경우

    print(lst[n])

