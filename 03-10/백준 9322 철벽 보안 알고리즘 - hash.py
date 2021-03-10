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
    for i in range(len(public2)):        # 제2 공개키가
        for j in range(len(public1)):    # 제1 공개키와 같을때
            if public2[i] == public1[j]:  #제 2 공개키 위치와 제 1 공개키 위치 저장
                result.append([i, j])
    for i in range(len(secret)):
        x, y = result.popleft()
        final[y] = secret[x]     #평문의 제2 공개키 위치는 암호문의 제1 공개키 위치
    for i in range(len(final)):
        print(final[i], end=" ")
    print()
