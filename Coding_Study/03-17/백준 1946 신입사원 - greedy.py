import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    grade = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    count = 1
    grade.sort(key=lambda x:x[0])     # 서류 점수 순위 오름차순 정렬  -> 자기 다음사람이 면접 순위 자기보다 낮으면 둘다 낮은거
    minV = grade[0][1]                # 서류1등의 면접 순위 
    for i in range(1, N):
        if grade[i][1] < minV:            # 면접점수 순위가 더 낮은 사람이 나온다면
            minV = grade[i][1]            # 면접점수 커트라인을 그 순위로 해주고
            count += 1                    # 뽑은사람 한명 추가
    print(count)
