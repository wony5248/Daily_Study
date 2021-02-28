T = int(input())
for i in range(T):
    p = list(input())
    n = int(input())
    arr = input()[1:-1].split(",")
    lst = []
    # print(arr)
    iserror = 0
    for j in range(len(arr)):
        lst.append(arr[j])

    for j in range(len(p)):
        if p[j] == "R":
            lst.reverse()
        elif p[j] == "D" and lst:
            lst.pop(0)
        elif p[j] == "D" and not lst:
            iserror = 1
            break

    if iserror == 0:
        print(lst)
    elif iserror == 1:
        print("error")