from collections import deque
for i in range(2):
    TC = int(input())
    strlst = input()
    stack = deque()
    for j in range(len(strlst)):
        if strlst[j] == "(" or strlst[j] == "{" or strlst[j] == "[" or strlst[j] == "<":
            stack.append(strlst[j])
        elif strlst[0] == ")" or strlst[0] == "]" or strlst[0] == "}" or strlst[0] == ">":
            break
        elif strlst[j] == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                break
        elif strlst[j] == "}":
            if stack[-1] == "{":
                stack.pop()
            else:
                break
        elif strlst[j] == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                break
        elif strlst[j] == ">":
            if stack[-1] == "<":
                stack.pop()
            else:
                break

    if stack:
        print("#%d %d" %(i+1, 0))
    else:
        print("#%d %d" % (i+1, 1))


