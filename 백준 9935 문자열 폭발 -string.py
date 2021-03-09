import sys
string = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())
# print(string)
# print(bomb)

for i in range(len(bomb)):
    result = ""
    for j in range(len(string)):
        if bomb[i] == string[j]:
            continue
        else:
            result += string[j]
    string = result
if not result:
    print("FRULA")
else:
    print(result)