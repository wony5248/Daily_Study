N = int(input())
li = list(map(int, input().split()))
idp, ddp = [1]*N, [1]*N
for i in range(1, N):
    if li[i] <= li[i-1]:
        idp[i] = max(idp[i], idp[i-1]+1)
    if li[i] >= li[i-1]:
        ddp[i] = max(ddp[i], ddp[i-1]+1)
print(max(max(idp), max(ddp)))