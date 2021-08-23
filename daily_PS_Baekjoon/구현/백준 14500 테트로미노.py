import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
paper = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
result1 = []

maxV = 0
for i in range(N): # 첫번째 모형 가로    ㅡ  ok
    for j in range(M-3):
        result1.append(sum(paper[i][j:j+4]))
for i in range(N-3):   # 1번째 모형 세로    ㅣ  ok
    for j in range(M): 
        result1.append((paper[i][j]) + paper[i+1][j] + paper[i+2][j] + paper[i+3][j])
for i in range(N-1): # 두번째 모형은 하나밖에 없음   ㅁ  ok
    for j in range(M-1):
        result1.append(sum(paper[i][j:j+2]) + sum(paper[i+1][j:j+2]))

for i in range(N-2):
    for j in range(M-1):
        result1.append((paper[i][j] + sum(paper[i+1][j:j+2]) + paper[i+2][j+1]))     # ㄴ위 +ㄱ아래 모양 ok
        result1.append(paper[i][j] + paper[i + 1][j] + sum(paper[i + 2][j:j + 2]))   # ㄴ 모양 ok
        result1.append(sum(paper[i][j:j+2]) + paper[i+1][j] + paper[i+2][j])         #ㄱ 반대 모양 ok
        result1.append(sum(paper[i][j:j+2]) + paper[i+1][j+1] + paper[i+2][j+1])          # ㄱ 모양  ok
        result1.append(paper[i][j] + sum(paper[i+1][j:j+2]) + paper[i+2][j])     # ㅏ 모양  ok

for i in range(N-1):
    for j in range(M-2):
        result1.append(sum(paper[i][j:j+3]) + paper[i+1][j+1])   # ㅜ 모양  ok
        result1.append(sum(paper[i][j:j+2]) + sum(paper[i+1][j+1:j+3]))   #ㄱㄴ  모양
        result1.append(paper[i][j] + sum(paper[i+1][j:j+3]))
        result1.append(paper[i+1][j] + sum(paper[i][j:j + 3]))
        result1.append(paper[i + 1][j+2] + sum(paper[i][j:j + 3]))
for i in range(2, N):
    for j in range(M-1):
        result1.append(sum(paper[i][j:j+2]) + paper[i-1][j+1] + paper[i-2][j+1])
for i in range(N-1):
    for j in range(1, M-1):
        result1.append(paper[i][j] + sum(paper[i+1][j-1:j+2]))   # ㅗ 모양
for i in range(1, N):
    for j in range(1, M-1):
        result1.append(sum(paper[i][j:j + 2]) + sum(paper[i - 1][j + 1:j + 3]))  # ㄴ 반대 왼 + ㄱ 반대 오
for i in range(1, N-1):
    for j in range(M-1):
        result1.append(sum(paper[i][j:j+2]) + paper[i-1][j+1] + paper[i+1][j+1])  # ㅓ 모양
        result1.append(sum(paper[i][j:j+2]) + paper[i+1][j] + paper[i-1][j+1])   #ㄴ반대위 + ㄱ반대아래

for i in range(N-1):
    for j in range(2, M):
        result1.append(paper[i][j] + sum(paper[i+1][j-2:j+1]))
        
        

print(max(result1))

