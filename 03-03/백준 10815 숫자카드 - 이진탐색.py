import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
M = int(input())
pick = list(map(int, sys.stdin.readline().split()))
for i in pick:
    if i in lst:
        print(1, end=" ")
    else:
        print(0, end=" ")
