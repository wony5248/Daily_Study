import sys
input = sys.stdin.readline
N = int(input())
M = int(input())


broken = set(input().rstrip().split())        # 고장난 버튼
result = abs(100 - N)
for i in range(1000001):             # 희망 채널은 500000까지 이지만 채널 자체는 무한대이기에 위에서 내려오는게 빠를지
    isflag = 0                       # 아래서 올라가는게 빠를지 다 해봐야함
    for j in str(i):
        if j in broken:              # 고장난 버튼에 있을때
            isflag = 1               # 이동하려는 번호에 고장난번호 포함시 1
            break
    if isflag == 0 and result > abs(N - i) + len(str(i)):        # 숫자 버튼으로 이동 가능한 번호이고 지금까지의 최소 이동보다 작으면
        result = abs(N - i) + len(str(i))


print(result)


