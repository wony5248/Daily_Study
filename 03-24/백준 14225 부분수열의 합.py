import sys
from itertools import combinations
N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
result = set()

for i in range(1, N+1):
    part = set(combinations(S, i))             # 1자리 부터 N자리까지 모든 부분수열 중복없이 추출
    part = list(part)
    for j in range(len(part)):                 # 부분 수열 다 돌면서
        result.add(sum(part[j]))               # 부분 수열의 합 result 에 넣어줌
count = 1
while True:
    if count not in result:                    # count 1부터 증가 시키다가 result 에 없는 count 나오면 count 출력 및 종료
        print(count)
        break
    count += 1