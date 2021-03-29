import sys
input = sys.stdin.readline
N = int(input())
stack = {}
result = []
for i in range(N):
    name, log = input().split()            # 이름하고 출입현황 dictionary로 저장
    stack[name] = log                      # 가장  최근 값으로 저장
for n, l in stack.items():
    if l == "enter":                       # enter면 아직 회사에 있는거
        result.append(n)
result.sort(reverse = True)
for i in range(len(result)):               
    print(result[i])
