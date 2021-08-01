N = int(input())
node = list(map(int, input().split()))
tree = [[0 for _ in range(N)] for _ in range(N)]
visit = [0 for _ in range(N)]
erase = int(input())
count = 0

def dfs(start):
    global count
    visit[start] = 1
    isLeaf = 1
    for i in range(N):
        if tree[start][i] == 1 and visit[i] ==0:      #연결된 다른 노드가 있다면 다음 노드 탐색 -> leafnode 아님
            dfs(i)
            isLeaf = 0
    if isLeaf == 1:                   # isLeaf가 1이면 for문 안 지나친 것이기에 더이상 탐색할 노드가 없다 -> leafnode
        count += 1


root = 0

for i in range(N):
    if node[i] == -1:                 # 입력 받은 값이 -1이면 그 index는 root node
        root = i
    else:                             # -1이 아니면 부모 노드와 자식노드 연결 상태 인접행렬상에 1로 표시
        tree[node[i]][i] = 1
        tree[i][node[i]] = 1
for i in range(N):                    # 지워지는 노드와 연결된 모든 연결 상태 인접행렬상에서 0으로 표시
    tree[i][erase] = 0
    tree[erase][i] = 0

dfs(root)

if root == erase:
    count = 0
    print(count)
else:
    print(count)
print(tree)