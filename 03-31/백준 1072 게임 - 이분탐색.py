X, Y = map(int, input().split())
per = int((Y * 100 / X) )
high = 1000000000
low = 0

while low <= high:
    mid = (low + high) // 2                             # 최대값과 최소를 반으로 나눠가면서 조건을 만족하는 판수를 찾음
    result = int(((Y + mid) * 100 / (X + mid)))         # *를 나중에 해주면 틀림       # 스터디때 질문 파이썬 int 원리?
    if result <= per:                                   # 승률이 아직 초기 승률과 같거나 작다면
        low = mid + 1
    else:                                               # 승률이 초기 승률보다 높다면
        high = mid - 1
        
if int(((Y+low) * 100 / (X+low))) <= per:               # 다 돌았는데 초기 승률보다 작거나 같다면
    print(-1)
else:
    print(low)




# X, Y = map(int,input().split())
# print(int(X * 100 / Y))
# print(int((X/Y) * 100))