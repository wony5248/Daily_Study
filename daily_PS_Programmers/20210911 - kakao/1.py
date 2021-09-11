def solution(id_list, report, k):
    answer = []
    user = dict()
    reported = dict()
    result = []
    report = list(set(report))
    for i in id_list:
        user[i] = 0
    for i in report:
        a, b = i.split()
        if b not in reported.keys():
            reported[b] = 1
        else:
            reported[b] += 1
    for i in reported:
        if reported[i] >= k:
            answer.append(i)

    for i in report:
        a, b = i.split()
        if b in answer:
            user[a] += 1
    for i in user.values():
        result.append(i)
    return result