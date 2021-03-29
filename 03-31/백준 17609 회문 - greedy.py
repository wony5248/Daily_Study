import sys
input = sys.stdin.readline
T = int(input().rstrip())
for i in range(T):
    slst = list(input().rstrip())
    rslst = list(reversed(slst))
    length = len(slst)

    ispalin = 0
    if slst == rslst:
        print(0)
    else:
        for j in range(length):
            x = slst.pop(j)
            rslst = list(reversed(slst))
            if slst == rslst:
                ispalin = 1
                break
            slst.insert(j, x)



        if ispalin == 1:
            print(1)
        else:
            print(2)

lst = ["A", "B", "C", "D"]
print(lst[::-1])

