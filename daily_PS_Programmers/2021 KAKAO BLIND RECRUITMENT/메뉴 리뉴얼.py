from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        tmp = []
        for j in orders:
            combi = combinations(sorted(j), i)
            tmp += combi
        result = Counter(tmp)
        if len(result) != 0 and max(result.values()) != 1:
            answer += ["".join(k) for k in result if result[k] == max(result.values())]

    return sorted(answer)