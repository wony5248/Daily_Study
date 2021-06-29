import sys
input = sys.stdin.readline

S = input().rstrip()
K = input().rstrip()
result = ""
for i in range(len(S)):
    if S[i].isalpha():
        result += S[i]

if K in result:
    print(1)
else:
    print(0)