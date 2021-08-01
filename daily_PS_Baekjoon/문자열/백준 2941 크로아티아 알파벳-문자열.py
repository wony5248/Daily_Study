string = input()
result = []
for i in range(len(string)):
    if string[i] == "=":
        if string[i-1] == "z":
            if string[i-2] == "d":
                result.pop()
                result.pop()
                result.append("dz")
    elif string[i] == "j":
        if string[i-1] == "l":
            result.pop()
            result.append("lj")
        elif string[i-1] == "n":
            result.pop()
            result.append("nj")
        else:
            result.append("j")
    elif string[i] == "-":
        continue
    else:
        result.append(string[i])

print(len(result))

