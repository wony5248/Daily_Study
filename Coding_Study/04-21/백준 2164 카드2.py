from collections import deque
N = int(input())
card = deque([i for i in range(1, N+1)])
while len(card) > 1:
    card.popleft()           # 제일 위 카드 버리고
    card.append(card.popleft())    # 그 다음 위 카드 맨 아래로

print(card[0])