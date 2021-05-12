import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    grade = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    count = 1
    grade.sort(key=lambda x:x[0])         # 서류심사 등수대로 정렬
    minV = grade[0][1]
    for i in range(1, N):
        if grade[i][1] < minV:            # 서류순서 높은애부터 탐색하면서 면접성적 비교
            minV = grade[i][1]            # minV가 면접등수보다 크다면 서류는 낮으나 면접은 높음
            count += 1
    print(count)