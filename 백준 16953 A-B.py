A, B = list(map(int, input().split()))
count = 1
while True:
    if B == A:
        break
    elif B < A or (B % 2 != 0 and B % 10 !=1):
        count = -1
        break
    elif B % 2 == 0:
        B //= 2
        count += 1
    elif B % 2 != 0:
        B //= 10
        count += 1

print(count)







