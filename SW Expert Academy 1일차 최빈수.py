T = int(input())
for i in range(T):
    Tnum = int(input())
    scorelst = list(map(int, input().split()))
    lst = [0 for _ in range(101)]
    for j in scorelst:
        lst[j] += 1
    result = max(lst)
    for k in range(100, -1, -1):
        if lst[k] == result:
            print("#%d %d" %(Tnum, k))
            break