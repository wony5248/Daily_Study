import sys
N, K = map(int, sys.stdin.readline().split())
string = [list(sys.stdin.readline().rstrip()[4:-4]) for _ in range(N)]

result = 0
if K < 5:
    result = 0
else:
    for i in range(N):
        print(len(string[i]))

print(string)