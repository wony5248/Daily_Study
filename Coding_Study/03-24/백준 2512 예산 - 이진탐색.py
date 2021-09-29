import sys
input = sys.stdin.readline
N = int(input())
budget = list(map(int, input().split()))
maxbud = int(input())
low = 0 # 가장 작은 값
high = max(budget)  # 가장 큰값


while low <= high:        # 이분 탐색
    tmp = 0
    mid = (low + high) // 2   # 가장 큰값과 가장 작은 값의 가운데부터 시작
    for i in range(len(budget)):
        if budget[i] >= mid:        # 기준보다 크다면 
            tmp += mid          # 기준 값을 더해줌
        else:              # 기준이 더 크다면
            tmp += budget[i]     # 지원요청 금액을 더해줌
    if tmp > maxbud:
        high = mid -1           # 더 크면 high를 mid-1로
    else:                  # 더 작으면 low를 mid +1로
        low = mid + 1            

print(high)

