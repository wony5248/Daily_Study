N, M = map(int, input().split())
count = 0
for i in range(N, M+1):
    isprime = 1

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            isprime = 0
            break
    if i == 1 or isprime == 0:
        pass
    elif i == 2 or isprime == 1:
        print(i)

