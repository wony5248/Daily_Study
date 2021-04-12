def solution(n, lost, reserve):
    count = n - len(lost)
    for i in range(len(lost)):
        if reserve.count(lost[i]) == 1:
            reserve.remove(lost[i])
            count += 1
        elif reserve.count(lost[i] - 1) == 1 and lost.count(lost[i] - 1) != 1:
            count += 1
            reserve.remove(lost[i] - 1)

        elif reserve.count(lost[i] + 1) == 1 and lost.count(lost[i] + 1) != 1:
            count += 1
            reserve.remove(lost[i] + 1)

    answer = count
    return answer