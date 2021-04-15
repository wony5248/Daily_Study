from collections import deque
graph = [[0 for _ in range(10)] for _ in range(10)]
visit = [[0 for _ in range(10)] for _ in range(10)]
stack = deque()
flag = 0
total = 0
for i in range(10):
    graph[i] = list(map(int, input()))

for i in range(10):
    for j in range(10):
        if graph[i][j] == 1 and flag == 0:
            stack.append([i,j])           # 처음 만나는 1의 좌표 stack에 push
            flag = 1
            stack.append([i,j])     # 마지막 좌표를 알아내기 위해 처음 좌표를 한번더 push  -> elif문에서 pop을 하기위해
            total += 1
        elif graph[i][j] == 1 and flag == 1:
            stack.pop()
            stack.append([i,j])   # 처음 만나는 1과 마지막으로 만나는 1의 좌표만 남기기 위해 1이면 stack에서 pop한후 현재 좌표 push
            total += 1            # total = 그래프 내의 모든 1의 개수

istri = 0
thirdx, thirdy = 0, 0
firstx, firsty = stack[0]
lastx, lasty = stack[1]
count = 0
zero = 0
if firsty+1 < 10 and graph[firstx][firsty+1] == 1:    # 첫 꼭지점 에서 오른쪽으로 이동 가능한 경우
    # print("here1")

    while graph[firstx][firsty + 1]:   # 첫 꼭지점에서 오른쪽으로 쭉 이동 마지막 좌표가 세번째 y좌표
        if firsty + 1 < 9:
            firsty += 1
        else:
            firsty += 1
            break
    thirdx = firstx
    thirdy = firsty
    stack.append([thirdx, thirdy])
    if stack[0][0] == thirdx and stack[1][1] == thirdy and thirdy - stack[0][1] == stack[1][0] - thirdx:   # 첫번째 삼각형 조건
        istri = 1
        for i in range(stack[1][0] - stack[0][0] + 1):        # 삼각형 내부를 탐색
            for j in range(i + 1):
                if graph[stack[1][0] - i][stack[1][1] - j] == 0: # 삼각형 내부에 0이 있다면 zero 를 증가
                    zero += 1
                else:                                           # 삼각형 내부에 0이 없다면(1이라면) count 증가 -> 삼각형을 이루는 1의 개수
                    count += 1
    elif stack[0][0] == thirdx and stack[0][1] == stack[1][1] and stack[1][0] - stack[0][0] == thirdy - stack[0][1]:   #두번째 삼각형 조건
        istri = 1
        for i in range(stack[1][0] - stack[0][0] + 1):
            for j in range(i + 1):
                if graph[stack[1][0] - i][stack[1][1] + j] == 0:
                    zero += 1
                else:
                    count += 1
    elif stack[0][0] == thirdx and stack[1][1] - stack[0][1] == thirdy - stack[1][1] and stack[1][1] - stack[0][1] == stack[1][0] - stack[0][0]: #세번째 삼각형 조건
        istri = 1
        for i in range(stack[1][0] - stack[0][0] + 1):
            for j in range(i + 1):
                if graph[stack[1][0] - i][stack[1][1] + j] == 0:
                    zero += 1
                if graph[stack[1][0] - i][stack[1][1] - j] == 0:
                    zero += 1
                if graph[stack[1][0] - i][stack[1][1] + j] == 1 and visit[stack[1][0] - i][stack[1][1] + j] == 0:   #이 경우에는 한 반복문 내에서 양쪽 탐색을 해야 하기에 양쪽 각각 count를 계산해줌 - 중복 탐색하는  부분은 visit을 이용하여 해결     -큰 직각 삼각형
                    count += 1
                    visit[stack[1][0] - i][stack[1][1] + j] = 1
                if graph[stack[1][0] - i][stack[1][1] - j] == 1 and visit[stack[1][0] - i][stack[1][1] - j] == 0:
                    count += 1
                    visit[stack[1][0] - i][stack[1][1] - j] = 1
elif graph[lastx][lasty-1] == 1:   # 마지막 꼭지점에서 왼쪽으로 이동 가능한 경우
    # print("here2")
    while graph[lastx][lasty-1]:   #마지막 꼭지점에서 왼쪽으로 쭉 탐색 마지막 좌표가 세번째 삼각형의y좌표
        if lasty - 1 > 0:
            lasty -= 1
        else:
            lasty -= 1
            break

    thirdx = lastx
    thirdy = lasty
    stack.append([thirdx, thirdy])
    if thirdx - stack[0][0] == stack[1][0] - stack[0][0] and stack[1][1] - stack[0][1] == stack[0][1] - thirdy and thirdx - stack[0][0] == stack[0][1] - thirdy:   #네번째 삼각형 조건
        istri = 1
        for i in range(stack[1][0] - stack[0][0] + 1):
            for j in range(i + 1):
                if graph[stack[0][0] + i][stack[0][1] + j] == 0:
                    zero += 1
                if graph[stack[0][0] + i][stack[0][1] - j] == 0:
                    zero += 1
                if graph[stack[0][0] + i][stack[0][1] + j] == 1 and visit[stack[0][0] + i][stack[0][1] + j] == 0:
                    count += 1
                    visit[stack[0][0] + i][stack[0][1] + j] = 1
                if graph[stack[0][0] + i][stack[0][1] - j] == 1 and visit[stack[0][0] + i][stack[0][1] - j] == 0:
                    count += 1
                    visit[stack[0][0] + i][stack[0][1] - j] = 1
    elif thirdy == stack[0][1] and thirdx == stack[1][0] and thirdx - stack[0][0] == stack[1][1] - thirdy:    # 다섯번째 삼각형 조건
        istri = 1
        for i in range(stack[1][0] - stack[0][0] + 1):
            for j in range(i + 1):
                if graph[stack[0][0] + i][stack[0][1] + j] == 0:
                    zero += 1
                count += 1

    elif thirdx == stack[1][0] and stack[0][1] == stack[1][1] and stack[1][1] - thirdy == stack[1][0] - stack[0][0]:    #6번째 삼각형 조건
        istri = 1
        for i in range(stack[1][0] - stack[0][0] + 1):
            for j in range(i + 1):
                if graph[stack[0][0] + i][stack[1][1] - j] == 0:
                    zero += 1
                else:
                    count += 1

else:  # 나머지 2개의 삼각형
    thirdx = (firstx + lastx) // 2
    maxgraph = max(graph)
    thirdy = maxgraph.index(1)
    rmaxgraph = reversed(maxgraph)
    thirdy1 = 9 - list(rmaxgraph).index(1)

    if thirdx - stack[0][0] == stack[1][0] - thirdx and stack[0][1] - thirdy == stack[1][1] - thirdy and stack[0][1] - thirdy == thirdx - stack[0][0]:  #7번째 삼각형 조건
        istri = 1
        stack.append([thirdx, thirdy])
        for i in range(stack[1][1] - thirdy + 1):
            for j in range(i + 1):
                if graph[thirdx + j][thirdy + i] == 0:
                    zero += 1
                if graph[thirdx - j][thirdy + i] == 0:
                    zero += 1
                if graph[thirdx + j][thirdy + i] == 1 and visit[thirdx + j][thirdy + i] == 0:
                    count += 1
                    visit[thirdx + j][thirdy + i] = 1
                if graph[thirdx - j][thirdy + i] == 1 and visit[thirdx - j][thirdy + i] == 0:
                    count += 1
                    visit[thirdx - j][thirdy + i] = 1

    elif stack[1][0] - thirdx == thirdx - stack[0][0] and thirdy1 - stack[0][1] == thirdy1 - stack[1][1] and thirdy1 - stack[0][1] == thirdx - stack[0][0]:   #8번째 삼각형 조건
        istri = 1
        stack.append([thirdx, thirdy1])
        for i in range(thirdy1 - stack[1][1] + 1):
            for j in range(i + 1):
                if graph[thirdx + j][thirdy1 - i] == 0:
                    zero += 1
                if graph[thirdx - j][thirdy1 - i] == 0:
                    zero += 1
                if graph[thirdx + j][thirdy1 - i] == 1 and visit[thirdx + j][thirdy1 - i] == 0:
                    count += 1
                    visit[thirdx + j][thirdy1 - i] = 1
                if graph[thirdx - j][thirdy1 - i] == 1 and visit[thirdx - j][thirdy1 - i] == 0:
                    count += 1
                    visit[thirdx - j][thirdy1 - i] = 1

lst = list(stack)
lst.sort()  #작은거부터 출력해야 하기에
if stack[0] == stack[1] or stack[1] == stack[2] or stack[0] == stack[2]:   # 한점이거나,직선일때
    print(0)
else:
    if istri == 1 and zero == 0 and count == total:    # 세좌표가 직각 삼각형이고, 내부에 0이 없고, 삼각형을 이루는 1의 갯수가 그래프 내의 전체 1의 갯수와 같다면
        for i in range(len(lst)):
            print(lst[i][0] + 1, lst[i][1] + 1)
    else:
        print(0)

# print(count, total, istri, zero)
# print(lst)




