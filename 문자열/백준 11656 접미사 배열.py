import sys
input = sys.stdin.readline
result = []
S = input().rstrip()
for i in range(len(S)):
    result.append(S[i:])

result.sort()
for i in result:
    print(i)