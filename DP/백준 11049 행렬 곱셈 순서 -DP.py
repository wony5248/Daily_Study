import sys
T = int(sys.stdin.readline())
final = []
for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    final.append([x, y])


def solve(p1, p2):
    if dp[p1][p2] != -1:
        return dp[p1][p2]
    else:
        minV = float("inf")
        for j in range(p1, p2, 1):
            minV = min(minV, solve(p1, j) + solve(j + 1, p2) + final[p1][0] * final[j][1] * final[p2][1] )
        dp[p1][p2] = minV
        return dp[p1][p2]


dp = [[-1 for _ in range(500)] for _ in range(500)]


for j in range(len(final)):
    for k in range(len(final)):
        if j == k:
            dp[j][k] = 0
solve(0, len(final) - 1)
print(dp[0][len(final) - 1])






