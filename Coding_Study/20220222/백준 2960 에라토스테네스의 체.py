import sys
import math
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
num = [i for i in range(2, N+1)]
visit = [0 for _ in range(N+1)]
cnt = 0
result = 0
isflag = 0

def isprime(n):
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True


for i in num:
    if visit[i] == 0 and isprime(i):
        for j in num:
            if visit[j] == 0 and j % i == 0:
                visit[j] = 1
                cnt += 1
            if cnt == K:
                result = j
                isflag = 1
                break
    if isflag:
        break


print(result)