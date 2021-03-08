import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())       # public2 -> public1 을 만드는 법 찾으면 됨
    public1 = sys.stdin.readline().rstrip().split()
    public2 = sys.stdin.readline().rstrip().split()
    secret = sys.stdin.readline().rstrip().split()
    result = deque()
    final = ["" for _ in range(n)]
    for i in range(len(public2)):
        for j in range(len(public1)):
            if public2[i] == public1[j]:
                result.append([i, j])
    for i in range(len(secret)):
        x, y = result.popleft()
        final[y] = secret[x]
    for i in range(len(final)):
        print(final[i], end=" ")
    print()
