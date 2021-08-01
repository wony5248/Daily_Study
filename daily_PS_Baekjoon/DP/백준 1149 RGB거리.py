import sys

N = int(sys.stdin.readline())

result = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
for i in range(1, len(result)):
    result[i][0] = min(result[i - 1][1], result[i - 1][2]) + result[i][0]
    result[i][1] = min(result[i - 1][0], result[i - 1][2]) + result[i][1]
    result[i][2] = min(result[i - 1][0], result[i - 1][1]) + result[i][2]
print(min(result[N - 1][0], result[N - 1][1], result[N - 1][2]))
# print(result)