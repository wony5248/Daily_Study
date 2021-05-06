import sys
input = sys.stdin.readline
while True:
    n = int(input().rstrip())
    if n == 0:
        break
    lst = [input().rstrip() for _ in range(n)]
    lst.sort(key=lambda x:x.upper())
    print(lst[0])