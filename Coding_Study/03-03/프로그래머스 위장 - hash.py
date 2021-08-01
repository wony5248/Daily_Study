name, kind = [list(input().split())]

def solution(clothes):

    lst = dict()
    for i in clothes:
        if i[1] in lst:             # 옷이 lst에 없다면 있다면 +1
            lst[i[1]] += 1
        else:                       # 옷이 lst에 없다면 그 옷의 갯수 1선언
            lst[i[1]] = 1
    answer = 1
    for i in lst.values():
        answer *= (i+1)          # 그냥 i 곱해주면 카테고리별로 하나만 입은경우 못셈
    return answer - 1