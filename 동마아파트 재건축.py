num = int(input())
apart = list(map(int, input().split()))
count = 1
for i in apart:
    if i > num:
        apart[i] = 0
for j in range(num, 0, -1):
    if apart[j] > apart[j - 1]:
        apart[j - 1] = apart[j]
    else:
        count += 1
print(count)

