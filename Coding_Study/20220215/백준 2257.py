import sys
dic = {"H":1, "C":12, "O":16}
input = sys.stdin.readline
poly = list(input().rstrip())
stack = []
for i in poly:
    if i.isalpha():
        stack.append(dic[i])
    elif i == "(":
        stack.append(i)
    elif i == ")":
        tmp = 0
        while True:
            x = stack.pop()

            if x == "(":
                break
            tmp += x
        if tmp == 0:
            continue
        else:
            stack.append(tmp)
    else:
        num = stack.pop()
        tmp2 = num * int(i)
        stack.append(tmp2)

print(sum(stack))
