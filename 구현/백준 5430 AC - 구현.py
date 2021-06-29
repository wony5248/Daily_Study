import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    p = list(input().rstrip())
    n = int(input())
    arr =input()[1:-2].split(",")
    lst = []
    iserror = 0
    isreverse = 0

    for j in range(len(p)):
        if p[j] == "R":
            isreverse = 1 - isreverse
        elif p[j] == "D" and arr:
            if isreverse == 1:
                arr.pop()
            else:
                arr.pop(0)
        elif p[j] == "D" and not arr:
            iserror = 1
            break
        if n == 0 and p[j] == "D":
            iserror = 1
            break

    if iserror == 0:
        if isreverse == 1:
            arr.reverse()
        print("[", end="")
        for j in range(len(arr)):
            if j == len(arr) - 1:
                print("%s" %arr[j], end="")
            else:
                print("%s," %arr[j], end="")
        print("]")
    elif iserror == 1:
        print("error")
