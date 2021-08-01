N, K = map(int, input().split())
lst = [True] * (N+1)
count = 0
for i in range(2, len(lst) + 1):
    for j in range(i, N+1, i):
        if lst[j] == True:
            lst[j] = False
            count += 1
            if count == K:
                print(j)
                break




