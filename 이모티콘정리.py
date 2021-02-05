N = int(input())
for i in range(N):
    imoticon = list(input())
    for j in range(2, len(imoticon)):
        if imoticon[j-2] == "(" and imoticon[j-1] == "(":
            imoticon[j-2] = ""
        if imoticon[j-1] == ")" and imoticon[j] == ")":
            imoticon[j-1] =  ""
        if imoticon[j-2] == "^" and imoticon[j-1] == "^" and imoticon[j] == "^":
            imoticon[j-2] = ""
        elif imoticon[j-2] == "^" and imoticon[j] == "^":
            imoticon[j-1] = "_"

for i in range(len(imoticon)):
    print(imoticon[i], end="")
