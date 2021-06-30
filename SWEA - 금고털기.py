T = int(input())
for tc in range(T):
    first = input()
    passwd = input()
    t0, t1, t2, t3 = 0, 0, 0, 0
    l0 = ord(first[0]) - ord(passwd[0])
    r0 = ord(passwd[0]) - ord(first[0])
    l1 = ord(first[1]) - ord(passwd[1])
    r1 = ord(passwd[1]) - ord(first[1])
    l2 = ord(first[2]) - ord(passwd[2])
    r2 = ord(passwd[2]) - ord(first[2])
    l3 = ord(first[3]) - ord(passwd[3])
    r3 = ord(passwd[3]) - ord(first[3])
    if l0 < 0:
        t0 = min((l0+26), r0)
    else:
        t0 = min(l0, (r0+26))
    if l1 < 0:
        t1 = min((l1+26) * 3, r1 * 2)
    else:
        t1 = min(l1 * 3, (r1+26) * 2)
    if l2 < 0:
        t2 = min((l2+26) * 5, r2 * 4)
    else:
        t2 = min(l2 * 5, (r2+26) * 4)
    if l3 < 0:
        t3 = min((l3+26) * 7, r3 * 6)
    else:
        t3 = min(l3 * 7, (r3+26) * 6)

    print("#%d %d" %(tc+1, t0+t1+t2+t3))

