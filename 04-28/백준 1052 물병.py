N, K = map(int, input().split())
bottle = [1 for _ in range(N)]
count = 0
while N > K:
    if N % 2 == 0:
        N = N // 2
    elif N % 2 == 1:
        N += 1
        count += 1


print(count)