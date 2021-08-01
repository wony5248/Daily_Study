import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
P = input().rstrip()
count = 0
result = 0
i = 0
while i < M-2:
    if P[i] == "I" and P[i+1] == "O" and P[i+2] == "I":   # IOI를 찾았을때
        count += 1                # count 1 증가
        if count == N:            # count가 N 이면  문자열이 있다는 거
            count -= 1            # 앞 IOI 빼줌
            result += 1           # 문자 갯수  하나 추가
        i += 1                    # IOI면 다음 I로 가기위해 인덱스 1 더 추가
    else:
        count = 0                 # IOI가 아니면 카운트 0으로 초기화
    i += 1
print(result)




# 시간초과 풀이
# import sys
# input = sys.stdin.readline
# N = int(input())
# M = int(input())
# P = input().rstrip()
# count = 0
# 
# for i in range(len(P)):
#     if P[i] == "I":
#         if P[i:i+N+1] == (P[i+N:i+(2*N) + 1][::-1]):
#             count += 1
# print(count)