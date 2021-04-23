N, K = map(int, input().split())
bottle = [1 for _ in range(N)]
count = 0
while N > K:
    if N % 2 == 0:
        N = N // 2
        bottle = list(map(lambda x: x*2, bottle[:N]))
    else:
        N += 1
        count += 1
        bottle.append(bottle[0])
    print(bottle)
print(count)