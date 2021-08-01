import sys
input = sys.stdin.readline
N = int(input())
P = list(map(int, input().split()))
count = 0
total = 0
P.sort()
for i in range(len(P)):                # 시간이 적게 걸리는 사람부터 이용하게 하면 최소시간
    count += P[i]
    total += count
print(total)