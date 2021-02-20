from collections import deque
N = list(map(int, input().split()))
t = int(input())

def solution(numbers, target):
    q = deque()
    q.append([numbers[0], 1])                  #queue에 +초깃값, 탐색횟수  랑  - 초깃값,  탐색횟수 넣어줌
    q.append([numbers[0] * (-1), 1])
    answer = 0
    while q:
        sum, index = q.popleft()
        if index == len(numbers):      # index 가 len(numbers)랑 같으면 끝까지 탐색한거
            if sum == target:          # target 이랑 같다면 answer +
                answer += 1
        else:
            q.append([sum + numbers[index], index+1])  # index가 len(numbers) 가 될때 까지 다음 값의 + 해주고 탐색
            q.append([sum - numbers[index], index+1])  # index가 len(numbers) 가 될때 까지 다음 값의 - 해주고
    return answer


print(solution(N, t))