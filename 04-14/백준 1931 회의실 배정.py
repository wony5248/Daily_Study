import sys
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    start, end = map(int, input().split())           # 배열에 [시작시간, 종료시간] 형식으로 넣어줌 
    lst.append([start, end])       

lst.sort(key= lambda x:(x[1],x[0]))                  # 종료시간순 으로 정렬하고 시작시간순 으로 정렬

result = 0
check = 0
for x, y in lst:
    if x >= check:             # 시작 시간이 전 회의 종료 시간보다 크면 -> 회의 가능   check 는 전 회의 종료 시간
        check = y
        result += 1
print(result)