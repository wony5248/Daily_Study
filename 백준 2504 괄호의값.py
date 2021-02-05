from collections import deque


strlst = input()
stack = deque()
check = deque()
count = 0
for j in range(len(strlst)):
    check.append(strlst[j])
    if strlst[j] == "(" or strlst[j] == "[":
        stack.append(strlst[j])
    elif strlst[0] == ")" or strlst[0] == "]":
        break
    elif strlst[j] == ")":
        if stack[-1] == "(":
            stack.pop()
        else:
            break
    elif strlst[j] == "]":
        if stack[-1] == "[":
            stack.pop()
        else:
            break

# if stack:
#     for i in range(1, len(check)):
#         if check[i]

print(check)


