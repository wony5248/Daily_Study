from collections import deque
graph = [[0 for _ in range(10)] for _ in range(10)]
stack = deque()
flag = 0
for i in range(10):
    graph[i] = list(map(int, input()))

for i in range(10):
    for j in range(10):
        if graph[i][j] == 1 and flag == 0:
            stack.append([i,j])           # 처음 만나는 1의 좌표 stack에 push
            flag = 1
            stack.append([i,j])           # 마지막 좌표를 알아내기 위해 처음 좌표를 한번더 push  -> elif문에서 pop을 하기위해
        elif graph[i][j] == 1 and flag == 1:
            stack.pop()
            stack.append([i,j])           # 처음 만나는 1과 마지막으로 만나는 1의 좌표만 남기기 위해 1이면 stack에서 pop한후 현재 좌표 push

istri = 0
thirdx, thirdy = 0, 0
firstx, firsty = stack[0]
lastx, lasty = stack[1]
if graph[firstx][firsty+1] == 1:    # 첫 꼭지점 에서 오른쪽으로 이동 가능한 경우
    # print("here1")
    while graph[firstx][firsty+1]:
        firsty += 1
    thirdx = firstx
    thirdy = firsty
    stack.append([thirdx, thirdy])
    if stack[0][0] == thirdx and stack[1][1] == thirdy and thirdy - stack[0][1] == stack[1][0] - thirdx:
        istri = 1
    elif stack[0][0] == thirdx and stack[0][1] == stack[1][1] and stack[1][0] - stack[0][0] == thirdy - stack[0][1]:
        istri = 1
    elif stack[0][0] == thirdx and stack[1][1] - stack[0][1] == thirdy - stack[1][1] and stack[1][1] - stack[0][1] == stack[1][0] - stack[0][0]:
        istri = 1
elif graph[lastx][lasty-1] == 1:   # 마지막 꼭지점에서 왼쪽으로 이동 가능한 경우
    # print("here2")
    while graph[lastx][lasty-1]:
        lasty -= 1
    thirdx = lastx
    thirdy = lasty
    stack.append([thirdx, thirdy])
    if thirdx - stack[0][0] == stack[1][0] - stack[0][0] and stack[1][1] - stack[0][1] == stack[0][1] - thirdy and thirdx - stack[0][0] == stack[0][1] - thirdy:
        istri = 1
    elif thirdy == stack[0][1] and thirdx == stack[1][0] and thirdx - stack[0][0] == stack[1][1] - thirdy:
        istri = 1
    elif thirdx == stack[1][0] and stack[0][1] == stack[1][1] and stack[1][1] - thirdy == stack[1][0] - stack[0][0]:
        istri = 1
else:  # 나머지 2개의 삼각형
    # print("here3")
    thirdx = (firstx + lastx) // 2
    thirdy = max(graph).index(1)
    stack.append([thirdx, thirdy])
    if thirdx - firstx == lastx - thirdx and firsty - thirdy == lasty - thirdy and firsty - thirdy == thirdx - firstx:
        istri = 1
    elif lastx - thirdx == thirdx - firstx and thirdy - firsty == thirdy - lasty and thirdy - firsty == thirdx - firstx:
        istri = 1

lst = list(stack)
lst.sort()
if stack[0] == stack[1] or stack[1] == stack[2] or stack[0] == stack[2]:
    print(0)
else:
    if istri == 0:
        print(0)
    elif istri == 1:
        for i in range(len(lst)):
            print(lst[i][0] + 1, lst[i][1] + 1)



