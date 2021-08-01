from collections import deque
length = int(input())
Weight = int(input())
truck = list(map(int, input().split()))
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    answer = 0
    queue = [0 for _ in range(bridge_length)]            # 다리의 길이 만큼 queue를 만들어줌
    while queue:                        # 한번돌때 1초
        queue.pop(0)                    # queue의 첫 원소 pop       
        if truck_weights:               # 들어올 트럭이 남았다면
            if sum(queue) + truck_weights[0] <= weight:   # queue의 합과 새로 들어올 트럭의 합이 다리무게보다 낮다면
                queue.append(truck_weights.popleft())     # queue에 차 추가
            else:                                # queue의 합 + 새로들어올  트럭 합이 다리무게 보다 높으면 0추가
                queue.append(0)                  # 결론적으로 1초에 다리위에 있는차가 한칸씩 왼쪽으로 당겨짐
        else:                       # 더이상 들어올 트럭이 없다면
            answer += bridge_length             #다리길이만큼 시간 추가해주고 break
            break
        answer += 1

    return answer


print(solution(length, Weight, truck))