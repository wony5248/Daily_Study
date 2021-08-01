N = int(input())
P = list(map(int, input().split()))
count = 0
total = 0
P.sort()
for i in range(len(P)):
    count += P[i]
    total += count
print(total)