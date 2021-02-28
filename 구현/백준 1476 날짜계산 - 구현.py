E, S, M = map(int, input().split())

ecount = 1
scount = 1
mcount = 1
count = 1
while True:

    if ecount == E and scount == S and mcount == M:
        break
    if ecount == 15:
        ecount = 0
    if scount == 28:
        scount = 0
    if mcount == 19:
        mcount = 0
    ecount += 1
    scount += 1
    mcount += 1
    count += 1

print(count)