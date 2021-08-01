from collections import deque
for k in range(1, 11):
    TC = int(input())
    num = list(map(int, input().split()))
    i = 0
    while True:
        a = num.pop(0)
        i += 1
        if i == 6:
            i = 1
        num.append(a-i)
        if a-i <= 0:
            num.pop()
            num.append(0)
            break
    print("#%d" %TC, end =" ")
    for j in range(len(num)):
        if j == 7:
            print(num[j])
        else:
            print(num[j], end=" ")

