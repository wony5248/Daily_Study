from collections import deque
N = list(map(int, input().split()))
t = int(input())

def solution(numbers, target):
    q = deque()
    q.append([numbers[0], 1])
    q.append([numbers[0] * (-1), 1])
    answer = 0
    while q:
        sum, index = q.popleft()
        if index == len(numbers):
            if sum == target:
                answer += 1
        else:
            q.append([sum + numbers[index], index+1])
            q.append([sum - numbers[index], index+1])
    return answer


print(solution(N, t))