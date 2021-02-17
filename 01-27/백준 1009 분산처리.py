import sys

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    rem = a % 10
    if rem == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        if b % 2 == 0:
            print(a ** 2 % 10)
        else:
            print(a)
    else:
        if b % 4 == 0:
            print(a ** 4 % 10)
        else:
            print(a ** (b % 4) % 10)