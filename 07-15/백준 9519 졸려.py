import sys
import copy
input = sys.stdin.readline
X = int(input())
string = list(input().rstrip())
original = copy.copy(string)
period = 0
# string = ["a" for _ in range(1000)]
tmp = ["" for _ in range(len(string))]

while True:
    tmp[0] = string[0]
    for i in range(1, len(string)):
        if i % 2 == 0:
            tmp[i // 2] = string[i]
        else:
            tmp[-(i//2 + 1)] = string[i]

    string = list("".join(tmp))
    period += 1
    if original == string:
        break

if X > period:
    X = X % period

while X:
    tmp[0] = string[0]
    for i in range(1, len(string)):
        if i % 2 == 0:
            tmp[i // 2] = string[i]
        else:
            tmp[-(i//2 + 1)] = string[i]

    string = list("".join(tmp))
    period += 1
    X -= 1
print("".join(string))
