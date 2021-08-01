T = int(input())


def solve1(start):                                # 찾고자하는 자식 두개로부터 두개의 모든 부모를 result1에 추가
    result1.append(start)
    for j in range(len(tree1[start])):
        solve1(tree1[start][j])



def size(start):                                  # 공통 부모(start) 입력 받으면 자식 수만큼 count 증가
    global count
    count += 1
    for j in range(len(tree2[start])):
        size(tree2[start][j])


for i in range(T):
    V, E, lastV1, lastV2 = map(int, input().split())
    tree1 = [[] for _ in range(V +1)]
    tree2 = [[] for _ in range(V +1)]
    count = 0
    final = []
    result1 = []
    edge = list(map(int, input().split()))
    for j in range(0, len(edge), 2):
        parent = edge[j]
        child = edge[j+1]
        tree1[child].append(parent)          # 자식 -> 부모로의 관계  - 공통 부모 구하는 용
        tree2[parent].append(child)          # 부모 -> 자식으로의 관계   - subtree크기 구하는용
    solve1(lastV1)
    solve1(lastV2)
    result1.pop(0)
    for j in result1:                        # result에 공통으로들어간 수들 뽑아냄 -> 공통 부모
        if result1.count(j) == 2:
            final.append(j)

    size(final[0])                           # 공통 부모중 가장 가까운 부모 final[0]

    print("#%d %d %d" % (i+1, final[0], count))




