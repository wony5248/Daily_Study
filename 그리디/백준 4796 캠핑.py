TC = 0
lst = [0, ]
while True:
    TC += 1
    L, P, V = list(map(int, input().split()))
    if L == 0 and P == 0 and V == 0:
        break
    rem = V // P
    rem1 = V % P
    if rem1 <= L:
        day = (L * rem) + (V % P)
    elif rem1 > L:
        day = (L * rem) + L
    lst.append(day)
    print("Case %d: %d" %(TC, lst[TC]))