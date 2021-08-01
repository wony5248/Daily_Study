T = int(input())

def solution(clothes):
    lst = dict()
    for j in clothes:
        if j in lst:             # 옷이 lst에 있다면 있다면 +1
            lst[j] += 1
        else:                       # 옷이 lst에 없다면 그 옷의 갯수 1선언
            lst[j] = 1
    answer = 1
    for j in lst.values():
        answer *= (j+1)          # 그냥 j 곱해주면 카테고리별로 하나만 입은경우 못셈
    return answer - 1

for i in range(T):
    clothes = []
    n = int(input())
    for j in range(n):
        name, kind = list(input().split())
        clothes.append(kind)
    print(solution(clothes))