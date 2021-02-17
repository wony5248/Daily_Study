import sys

maxDistance = int(sys.stdin.readline())    # 정비  없이 갈 수 있는 최대거리
num = int(sys.stdin.readline())    # 정비소 수
distance = list(map(int, sys.stdin.readline().split()))    # 정비소 간의 거리
time = list(map(int, sys.stdin.readline().split()))    # 정비하는데 걸리는 시간

time.insert(0, 0)      # 출발지와 도착지에서는 시간이 0이기에 양쪽끝에 0 추가
time.append(0)
choose = [[0, []] for _ in range(num + 2)]    # 들린 정비소에서 걸린 시간, [들린 정비소 번호]

choose[1][0] = time[1]   # 첫번째 정비소에서 걸리는 시간

for i in range(2, num + 2):     # n번째 정비소 기준 before = n-1번째 정비소   ->
    before = i-1                # n번기준 maxdistance 내의 정비소 돌면서 최소시간 걸리는거 찾아냄
    temp = choose[before][0]      # n-1번째 정비소 고를때 시간
    dist = distance[before]      # n 번째에서 n-1번째 정비소 까지의 거리
    for j in range(before-1, -1, -1):   # n-2번째 부터 출발지 까지
        dist += distance[j]       
        if maxDistance < dist:           
            break              
        if choose[j][0] < temp:     # n-2번째 정비소의 시간이 현재 저장되어있는 n-1번째 정비소의 시간보다 작을때
            temp = choose[j][0]     # 이 정비소를 선택함
            before = j          # 좌표를 정비소로 이동
    choose[i][0] = temp + time[i]  # 지금까지 선택한 정비소의 시간에 선택한 정비소의 시간을 더해줌
    if before:
        choose[i][1] = choose[before][1] + [before]   # 고른 정비소 추가

print(choose[-1][0])
print(len(choose[-1][1]))
print(" ".join(map(str, choose[-1][1])))



    
