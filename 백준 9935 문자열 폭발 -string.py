import sys
string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()


result = ""
while True:
    if bomb not in string:
        break
    else:
        result = string[:string.find(bomb)] + string[string.find(bomb) + len(bomb):]
        string = result

if result:
    print(result)
else:
    print("FRULA")


