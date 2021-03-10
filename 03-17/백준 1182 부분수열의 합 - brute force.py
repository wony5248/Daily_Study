import sys
from itertools import combinations
input = sys.stdin.readline
N, S = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
count = 0
result = []
for i in range(1,N+1):   # 1 ~ N 까지
    result = list(combinations(lst, i))   # 1~ N개 의 수로 만들수 있는 모든 부분수열 1개일때, 2개일때 3개일때 ~~
    for j in range(len(result)):
        if sum(result[j]) == S:          # 부분수열의 합이 S면 count + 1
            count += 1
print(count)