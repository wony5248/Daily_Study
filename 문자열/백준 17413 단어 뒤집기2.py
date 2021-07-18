string = list(input())
idx = 0
stack = []
result = []
while idx < len(string):
    if string[idx] == "<":
        if stack:
            result.append("".join(stack[::-1]))
            stack = []
        stack.append(string[idx])
        idx += 1
        while string[idx] != ">":
            stack.append(string[idx])
            idx += 1
        stack.append(">")
        idx += 1
        result.append("".join(stack))
        stack = []
    elif string[idx] == " ":
        if stack:
            result.append("".join(stack[::-1]))
        result.append(" ")
        stack = []
        idx += 1
    else:
        stack.append(string[idx])
        idx += 1
result.append("".join(stack[::-1]))

print("".join(result))