import sys
input = sys.stdin.readline
N = int(input())
lst = [input().rstrip().split() for _ in range(N)]

lst.sort(key= lambda x : int(x[0]))

for i in lst:
    print("%s %s" %(i[0], i[1]))