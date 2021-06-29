N = list(input())
N.sort(reverse = True)
num = "".join(N)
if int(num) % 30 == 0:
    print(num)
else:
    print(-1)
