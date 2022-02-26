from itertools import combinations


def solution(relation):
    answer = []

    length = len(relation[0])
    arr = [i for i in range(length)]
    for i in range(1, length + 1):  # 몇개의 후보키를 뽑는지
        for com in combinations(arr, i):  # i개의 후보키 뽑았을때
            arr2 = []
            isfalse = 0
            for re in relation:  # 각 행
                cur = []  # 각 행의 후보키 값들
                for x in com:
                    cur.append(re[x])
                if cur in arr2:
                    isfalse = 1
                    break
                else:
                    arr2.append(cur)
            if isfalse == 0:
                isflag = 0
                for l in answer:
                    if set(l).issubset(set(com)):
                        isflag = 1
                        break
                if isflag == 0:
                    answer.append(com)

    return len(answer)