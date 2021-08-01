import sys
string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

last = bomb[-1]
stack = []
result = ""
for i in string:
    stack.append(i)
    if i == last and "".join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

result = "".join(stack)


if result:
    print(result)
else:
    print("FRULA")


