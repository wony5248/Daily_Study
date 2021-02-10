N, total = map(int, input().split())
coin = [0 for _ in range(N)]
for i in range(N):
    coin[i] = int(input())
count = 0
while True:
    if total <= 0:
        break
    elif coin[-1] > total:
        coin.pop()
    else:
        count += total // coin[-1]
        total = total % coin[-1]

print(count)
