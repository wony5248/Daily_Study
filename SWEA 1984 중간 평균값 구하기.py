import math
T = int(input())
for i in range(T):
    N = list(map(int, input().split()))
    lst = []
    for j in range(len(N)):
        if N[j] == max(N):
            continue
        elif N[j] == min(N):
            continue
        else:
            lst.append(N[j])
    avg = sum(lst) / len(lst)
    print("#%d %d" %(i+1, round(avg) ))

