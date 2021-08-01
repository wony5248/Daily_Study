import sys
N, total = map(int, sys.stdin.readline().rstrip().split())
coin = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

count = 0
while total:                # total 이 0미만 일때까지 반복
    if coin[-1] > total:    # 가지고 있는 가장 큰 금액이 total보다 크면 그돈은 뺌
        coin.pop()
    else:
        count += total // coin[-1]    # 아닌경우 total을 가장큰 금액 단위로 나눠줌
        total = total % coin[-1]      # 몫은 동전 개수(count)이고 나머지는 total
        coin.pop()                    # 가진 동전 목록에서 빼줌

print(count)
