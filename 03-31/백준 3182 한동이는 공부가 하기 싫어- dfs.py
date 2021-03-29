N = int(input())
senior = [0 for _ in range(N+1)]
result = [0,]


def dfs(start):
    global tmp
    tmp += 1
    visit[start] = 1
    if senior[start] != 0 and visit[senior[start]] == 0:   # 0 이면 아는 사람 X 
        visit[senior[start]] = 1
        dfs(senior[start])


for i in range(1, N+1):
    x = int(input())
    senior[i] = x
for i in range(1, N+1):        # 1번부터 N번 선배 까지 다 물어보고 아는 선배 제일 많은 선배 찾기
    visit = [0 for _ in range(N+1)]
    tmp = 0
    dfs(i)
    result.append(tmp)


print(result.index(max(result)))