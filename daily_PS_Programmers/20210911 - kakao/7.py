a = ["muzi", "frodo", "apeach", "neo"]
b = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
c = 2
def solution(id_list, report, k):
    answer = []
    user = dict()
    reported = dict()
    for i in range(report):
        a, b = i.split()
        if b not in reported.keys():
            reported[b] = 1
        else:
            reported[b] += 1
    print(reported)
    return answer

solution(a, b, c)