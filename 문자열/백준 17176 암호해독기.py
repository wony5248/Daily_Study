import sys
input = sys.stdin.readline
result = []
N = int(input().rstrip())
secret = list(map(int, input().rstrip().split()))
normal = list(input().rstrip())
for i in secret:
    if i == 0:
        result.append(" ")
    elif 1 <= i <= 26:
        result.append(chr(i+64))
    elif 27 <= i <= 52:
        result.append(chr(i+70))

result.sort()
normal.sort()


if normal == result:
    print("y")
else:
    print("n")