from collections import deque
p = list(map(int, input().split()))
loc = int(input())
def solution(priorities, location):
    answer = 0

    queue = deque()
    for i in range(len(priorities)):
        queue.append([priorities[i], i])    # 같은수 처리하기 위해 index를 같이 넘겨줌 -> [우선순위, 초기 위치]
    while len(queue):
        prior, loc = queue.popleft()           # waiting queue에서 빼줌
        if queue and prior < max(queue)[0]:    # 우선순위가 제일 높지 않다면
            queue.append([prior, loc])         # 맨뒤로 보냄
        else:                                  # 우선순위 제일 높다면 출력
            answer += 1                        # answer + 1   ->  출력순서
            if loc == location:                # 출력한 것의 loc가 location이랑 같다면 끝 -> answer 는 출력순서
                break
    return answer



print(solution(p, loc))