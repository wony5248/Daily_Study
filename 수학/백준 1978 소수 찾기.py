N = int(input())
num = list(map(int, input().split()))
count = 0
for i in num:
    isprime = 1

    for j in range(2, i):
        if i % j == 0:
            isprime = 0
    if i == 1 or isprime == 0:
        pass
    elif i == 2 or isprime == 1:
        count += 1

print(count)