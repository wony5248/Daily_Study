import sys
N, K = map(int, sys.stdin.readline().split())
string = [list(sys.stdin.readline().rstrip()[4:-4]) for _ in range(N)]
for i in range(N):
    for j in range(len(string[i])):
        if string[i][j] == "a" or string[i][j] == "n" or string[i][j] == "t" or string[i][j] == "i" or string[i][j] == "c":
            string[i].pop(j)
            string[i].insert(j, "0")
result = 0
if K < 5:
    result = 0


# 97~122
print(string)