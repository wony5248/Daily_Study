def solution(research, n, k):
    answer = ''
    lst = []
    dic = dict()
    for i in range(97, 123, 1):
        dic[chr(i)] = 0
    for i in range(0, len(research)-n+1, 1):
        for j in range(97, 123, 1):
            isissue = 0
            cnt = 0
            for l in range(i, i+n):
                if research[l].count(chr(j)) >= k:
                    cnt += research[l].count(chr(j))
                else:
                    isissue = 1
            if isissue == 0:
                if cnt >= 2 * n * k:
                    lst.append(chr(j))
    lst.sort()
    for i in lst:
        dic[i] += 1
    if max(dic.values()) == 0:
        answer = "None"
    else:
        answer = max(dic, key=dic.get)
    return answer