import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pedia = {}

for i in range(1, N+1):
    pedia[i] = input().rstrip()                  # 번호 : 포켓몬 이름  형태로 저장
rpedia = dict(map(reversed, pedia.items()))      # 포켓몬 이름: 번호 형태로 저장       -> key value를  반대로 map해줌
for i in range(M):               
    x = input().rstrip() 
    if x.isdecimal():                # 입력받은게 숫자라면
        print(pedia[int(x)])         # 기본 도감에서 해당 번호 포켓몬 출력
    else:
        print(rpedia[x])             # 반전된 도감에서 해당 이름의 포켓몬의 번호 출력

