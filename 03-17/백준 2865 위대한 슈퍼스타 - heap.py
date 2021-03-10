import sys

input = sys.stdin.readline
N, M, K = map(int, input().rstrip().split())
result = [[] for _ in range(N)]
final = []
for _ in range(M):
    lst = list(map(float, input().rstrip().split()))
    for j in range(0, N * 2, 2):     # 사람별로 점수 모아줌 N번 스타의 M개 장르의 대한 점수가 하나의 list
        result[int(lst[j])-1].append(lst[j+1])

for i in range(K):                     # 최댓값 K개 뽑아내기 위해 
    maxV = 0
    isflag = 0
    for j in range(N):
        for k in range(M):
            if maxV < result[j][k]:           #최고점을 찾아서 maxV에 넣어줌
                maxV = result[j][k]
    for j in range(N):
        if isflag == 1:                      # K번째 반복에서 최댓값 이미 찾음 -> K+1번째로 가자
            break
        for k in range(M):
            if result[j][k] == maxV:         # 최고점이면 
                final.append(maxV)           # 최고점수 기록
                result[j] = [0 for _ in range(M)]   #그 스타의 모든 점수 0으로 초기화
                isflag = 1                   # 최고점수 찾았다는 의미
                break                        
print(round(sum(final), 1))
# print(result)
