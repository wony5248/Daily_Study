from collections import deque

p = list(map(int, input().split()))
l = int(input())
def solution(people, limit):
    answer = 0

    people.sort()
    queue = deque(people)
    while queue:
        if len(queue) >= 2 and queue[0] + queue[-1] <= limit:
            answer += 1
            queue.pop()
            queue.popleft()
        else:
            queue.pop()
            answer += 1

    return answer




print(solution(p, l))