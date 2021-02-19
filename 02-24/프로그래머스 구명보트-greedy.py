from collections import deque           #list로 하니 시간초과

p = list(map(int, input().split()))
l = int(input())
def solution(people, limit):
    answer = 0

    people.sort()     # 사람 낮은 ->높은 무게순으로 정렬
    queue = deque(people)
    while queue:
        if len(queue) >= 2 and queue[0] + queue[-1] <= limit:   #가장 가벼운 무게랑 무거운 무게랑 더해서 보트 무게보다 낮을시
            answer += 1                 # 보트 한대 추가
            queue.pop()                 # 사람 두명 뺌
            queue.popleft()
        else:                           # 보트무게 넘을시 -> 가장 무거운 무게의 사람만 빼줌
            queue.pop()
            answer += 1

    return answer




print(solution(p, l))