import sys
input = sys.stdin.readline
result = 0
N = int(input())
lst = [list(map(int, input().rstrip().split())) for _ in range(N)]
for i in range(len(lst)-1):                      # x 기준 오름차순 이므로 다음 선분의 왼쪽 좌표가 전 선분의 오른쪽 좌표보다 작으면
    if lst[i][1] >= lst[i+1][0]:                 #  두 선분은 같은 선분 -> 합쳐준다.
        lst[i+1][0] = lst[i][0]
        lst[i+1][1] = max(lst[i+1][1], lst[i][1])
    else:
        result += abs(lst[i][1] - lst[i][0])

result += abs(lst[-1][1] - lst[-1][0])
print(result)