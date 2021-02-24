number = int(input())
Lost = list(map(int, input().split()))
Reserve = list(map(int, input().split()))

def solution(n, lost, reserve):
    count = n - len(lost)                 # count 초깃값은 총 학생수 에서 체육복 없는애들 빼줌
    for i in range(len(lost)):
        if reserve.count(lost[i]) == 1:           # 잃어버린 애랑 여벌 옷 가진애랑 겹칠때
            reserve.remove(lost[i])
            count += 1
        elif reserve.count(lost[i] - 1) == 1 and lost.count(lost[i] - 1) != 1:   # 잃어버린애 왼쪽애가 여벌옷 있을때
            count += 1                    # 체육 들을 수  있는애 한명 추가
            reserve.remove(lost[i] - 1)   # reseve에 여벌옷 가진애 없애줌

        elif reserve.count(lost[i] + 1) == 1 and lost.count(lost[i] + 1) != 1:   # 잃어버린애 오른쪽 애가 여벌옷 있을때
            count += 1
            reserve.remove(lost[i] + 1)

    answer = count
    return answer

print(solution(number, Lost, Reserve))