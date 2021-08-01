N = int(input())
count = 0

for i in range(1, N+1):
    hund = i // 100
    ten = (i - (hund * 100)) // 10
    one = i - (hund * 100) - (ten * 10)
    if i >= 100 and hund - ten == ten - one:
        count += 1
    elif i < 100:
        count += 1

print(count)