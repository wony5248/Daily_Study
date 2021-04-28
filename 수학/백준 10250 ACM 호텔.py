T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    if N // H < 9 and N % H != 0:
        print(str(N % H) + "0" + str((N // H) + 1))
    elif N // H >= 9 and N % H != 0:
        print(str(N % H) + str((N // H) + 1))
    elif N // H < 10 and N % H == 0:
        print(str(H) + "0" + str((N // H)))
    elif N // H >= 10 and N % H == 0:
        print(str(H) + str((N // H)))