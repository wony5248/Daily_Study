# 이 모임에는 몇 사람을 통하면 모두가 서로 알 수 있다는 조건이 있음
member = int(input())
rel =[[100 for _ in range(member+1)] for _ in range(member+1)]
result = []




while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break
    else:
        rel[a][b] = 1        #a 와 b는 친구 < = > b 와 a도 친구
        rel[b][a] = 1

for i in range(1, member +1):
    rel[i][i] = 0

for i in range(1, member+1):   # 거쳐가는 친구
    for j in range(1, member+1):  # 회원
        for k in range(1, member+1):  # 회원의 친구
            if rel[j][k] > rel[j][i] + rel[i][k]:    # j  ->  k로 바로 연결된 친구가 아닐때 중간의 껴 있는 친구의 수만큼 저장
                rel[j][k] = rel[j][i] + rel[i][k]    # 예제에서 i, j, k가 2 1 3 일때 1,3 은100이고 1, 2 는 1이고 2, 3은 1이라서 rel[1][3] = 2로 초기화

for i in range(1, member + 1):
    result.append(max(rel[i][1:]))  # 패딩 입혀서 0번째 인덱스는 더미값 100이 들어 있음
                                    # max로 추출하면 각 회원의 최대 점수를 얻을 수 있음(몇 사람 통하면 모두가 서로 안다는 조건이 있기에)
print(rel)
minvalue = min(result)    # 각 회원의 점수중 최소점을 얻음
print(minvalue, result.count(minvalue))  # 최소점과 최소점을얻은 모든 회원의 수 출력


for i in range(len(result)):
    if result[i] == minvalue:
        print((i+1), end=" ")  # 최소점이랑 같은 회원 인덱스 출력