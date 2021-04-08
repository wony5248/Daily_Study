import sys
string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()


result = ""
while True:
    if bomb not in string:
        break
    else:
        x = string.find(bomb)
        result = string[:x] + string[x + len(bomb):]
        string = result

if result:
    print(result)
else:
    print("FRULA")


