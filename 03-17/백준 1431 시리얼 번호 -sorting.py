import sys
N = int(sys.stdin.readline().rstrip())
guitar = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
sumV = [0 for _ in range(N)]       # 각  시리얼 번호의 숫자 합 기록할 배열

for i in range(N):
    for j in range(len(guitar[i])):
        if guitar[i][j].isdecimal():          # 각 시리얼 번호에서 숫자라면
            sumV[i] += int(guitar[i][j])      # 그 시리얼 번호의 다른 배열에 숫자만 더해줌
for i in range(N):
    guitar[i].append(sumV[i])                # 각 시리얼 번호의 숫자 합을 맨뒤에 추가해줌


guitar.sort(key=lambda x: (len(x), x[-1], x))   # 길이가 짧은거 부터 -> 숫자합이 작은거 부터 -> 사전식
# for i in range(N):
for i in range(N):
    for j in range(len(guitar[i]) - 1):    # 마지막에 숫자합 추가되어 있으므로 -1 까지
        print(guitar[i][j], end="")
    print()
