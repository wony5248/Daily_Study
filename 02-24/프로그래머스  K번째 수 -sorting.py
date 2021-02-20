# A = list(map(int, input().split()))
# com = [[list(map(int, input().split()))]]
def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        lst = array[commands[i][0] -1:commands[i][1]]    # commands 가 i j k 일때 i부터 j 까지 split
        lst.sort()
        answer.append(lst[commands[i][2]-1])   # sort후에  k-1번째 인덱스 answer에 추가
    return answer