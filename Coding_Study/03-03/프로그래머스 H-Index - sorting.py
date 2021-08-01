lst = list(map(int, input().split()))

def solution(citations):
    citations.sort()    # 뒤부터 탐색해주려고 sort함 - 가능한 Hindex중 가장 커야 하기에
    answer =0
    for i in range(max(citations), -1, -1):    # i = h를 의미 max부터 1씩 작게 하면서 탐색
        hindex = 0      # h번 이상 인용된 논문 수
        lindex = 0      # h번 이하 인용된 논문 수
        for j in range(len(citations)):
            if citations[j] >= i:         # 논문 다 돌면서 i 이상이면 hindex + 1
                hindex += 1
            if citations[j] <= i:         # 논문 다 돌면서 i 이하면 lindex + 1
                lindex += 1
        if hindex >= i and lindex <= i:   # hindex가 h 이상이고 lindex가 h 이하면
            answer = i                    # h = i = 가장 큰 수 부터 탐색했기에 처음나오는 i가 최대
            break



    return answer



print(solution(lst))
