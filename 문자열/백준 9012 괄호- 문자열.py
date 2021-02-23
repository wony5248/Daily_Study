T = int(input())


for i in range(T):
    stack = []
    isflag = 0
    lst = input()
    for j in range(len(lst)):
        if lst[j] == "(":
            stack.append(lst[j])
        elif lst[j] == ")" and stack:
            stack.pop()
        elif lst[j] == ")" and not stack:
            isflag = 1
            continue
    if stack or isflag == 1:
        print("NO")
    else:
        print("YES")
