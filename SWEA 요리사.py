from itertools import combinations
T = int(input())
for tc in range(T):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]
    result = 99999999
    for s1 in combinations(range(N), N//2):
        s2 = [i for i in range(N) if i not in s1]
        sum1 = 0
        sum2 = 0
        for i in range(N//2 - 1):
            for j in range(i+1, N//2):
                sum1 += food[s1[i]][s1[j]] + food[s1[j]][s1[i]]
                sum2 += food[s2[i]][s2[j]] + food[s2[j]][s2[i]]
        tmp = abs(sum2 - sum1)
        if result > tmp:
            result = tmp
    print("#%d %d" %(tc+1, result))