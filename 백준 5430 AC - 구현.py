import sys
T = int(input())
for i in range(T):
    p = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()[1:-1].split(",")
    lst = []
    # print(arr)
    iserror = 0
    for j in range(len(arr)):
        lst.append(arr[j])
    # print(lst)
    for j in range(len(p)):
        if p[j] == "R":
            lst.reverse()
        elif p[j] == "D" and lst:
            lst.pop(0)
        elif p[j] == "D" and len(lst) == 0:
            iserror = 1
            break
        if n == 0 and p[j] == "D":
            iserror = 1
            break

    if iserror == 0:
        print("[", end="")
        for j in range(len(lst)):
            if j == len(lst) - 1:
                print("%s]" %lst[j])
            else:
                print("%s," %lst[j], end="")
    elif iserror == 1:
        print("error")
